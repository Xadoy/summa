use summa_core::directories::{ExternalRequest, ExternalResponse, Header};
use summa_core::errors::SummaResult;
use tokio::sync::mpsc::unbounded_channel;
use wasm_bindgen::prelude::*;
use wasm_bindgen::JsValue;
use wasm_bindgen_futures::spawn_local;

#[wasm_bindgen(raw_module = "../src/gate.ts")]
extern "C" {
    #[wasm_bindgen(catch)]
    pub fn request(method: String, url: String, headers: JsValue) -> Result<JsValue, JsValue>;

    #[wasm_bindgen(catch)]
    pub async fn request_async(method: String, url: String, headers: JsValue) -> Result<JsValue, JsValue>;
}

#[derive(Clone, Debug)]
pub struct JsExternalRequest {
    pub method: String,
    pub url: String,
    pub headers: Vec<Header>,
}

#[async_trait]
impl ExternalRequest for JsExternalRequest {
    fn new(method: &str, url: &str, headers: &[Header]) -> Self
    where
        Self: Sized,
    {
        JsExternalRequest {
            method: method.to_string(),
            url: url.to_string(),
            headers: Vec::from_iter(headers.iter().cloned()),
        }
    }

    fn request(&self) -> SummaResult<ExternalResponse> {
        let response = request(
            self.method.to_string(),
            self.url.to_string(),
            serde_wasm_bindgen::to_value(&self.headers).unwrap(),
        )
        .map_err(|e| summa_core::Error::External(format!("{:?}", e)))?;
        let response: ExternalResponse = serde_wasm_bindgen::from_value(response).unwrap_throw();
        Ok(response)
    }

    async fn request_async(&self) -> SummaResult<ExternalResponse> {
        let (sender, mut receiver) = unbounded_channel();
        let method = self.method.to_string();
        let url = self.url.to_string();
        let headers = self.headers.clone();
        spawn_local(async move {
            let headers = serde_wasm_bindgen::to_value(&headers).unwrap();
            let response = request_async(method, url, headers)
                .await
                .map(|response| serde_wasm_bindgen::from_value(response).unwrap_throw())
                .map_err(|e| summa_core::Error::External(format!("{:?}", e)));
            sender.send(response).unwrap_throw();
        });
        let request_response = receiver.recv().await.unwrap_throw()?;
        Ok(request_response)
    }
}