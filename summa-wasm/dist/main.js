!function(e,n){"object"==typeof exports&&"object"==typeof module?module.exports=n():"function"==typeof define&&define.amd?define("summa-wasm",[],n):"object"==typeof exports?exports["summa-wasm"]=n():e["summa-wasm"]=n()}(self,(()=>(()=>{"use strict";var e={1:(e,n)=>{Object.defineProperty(n,"__esModule",{value:!0}),n.ChunkedCacheConfig=n.NetworkConfig=void 0;n.NetworkConfig=function(e,n,t,r){this.method=e,this.url_template=n,this.headers_template=t,this.chunked_cache_config=r};n.ChunkedCacheConfig=function(e,n){this.chunk_size=e,this.cache_size=n}},655:(e,n)=>{function t(e){var n=e.getAllResponseHeaders().toLowerCase().trim().split(/[\r\n]+/),t=[];return n.forEach((function(e){var n=e.split(": "),r=n.shift(),o=n.join(": ");t.push({name:r,value:o})})),t}n.I0=n.WY=void 0,n.WY=function(e,n,r){var o=new XMLHttpRequest;if(o.responseType="arraybuffer",o.open(e,n,!1),void 0!==r&&r.forEach((function(e){o.setRequestHeader(e.name,e.value)})),o.send(null),o.status>=200&&o.status<300)return{data:new Uint8Array(o.response),headers:t(o)};throw{status:o.status,status_text:o.statusText}},n.I0=function(e,n,r){return new Promise((function(o,i){var a=new XMLHttpRequest;a.responseType="arraybuffer",a.open(e,n),void 0!==r&&r.forEach((function(e){a.setRequestHeader(e.name,e.value)})),a.onload=function(){this.status>=200&&this.status<300?o({data:new Uint8Array(a.response),headers:t(a)}):i({status:this.status,status_text:a.statusText})},a.onerror=function(){i({status:this.status,status_text:a.statusText})},a.send()}))}},851:function(e,n,t){var r=this&&this.__awaiter||function(e,n,t,r){return new(t||(t=Promise))((function(o,i){function a(e){try{c(r.next(e))}catch(e){i(e)}}function u(e){try{c(r.throw(e))}catch(e){i(e)}}function c(e){var n;e.done?o(e.value):(n=e.value,n instanceof t?n:new t((function(e){e(n)}))).then(a,u)}c((r=r.apply(e,n||[])).next())}))},o=this&&this.__generator||function(e,n){var t,r,o,i,a={label:0,sent:function(){if(1&o[0])throw o[1];return o[1]},trys:[],ops:[]};return i={next:u(0),throw:u(1),return:u(2)},"function"==typeof Symbol&&(i[Symbol.iterator]=function(){return this}),i;function u(u){return function(c){return function(u){if(t)throw new TypeError("Generator is already executing.");for(;i&&(i=0,u[0]&&(a=0)),a;)try{if(t=1,r&&(o=2&u[0]?r.return:u[0]?r.throw||((o=r.return)&&o.call(r),0):r.next)&&!(o=o.call(r,u[1])).done)return o;switch(r=0,o&&(u=[2&u[0],o.value]),u[0]){case 0:case 1:o=u;break;case 4:return a.label++,{value:u[1],done:!1};case 5:a.label++,r=u[1],u=[0];continue;case 7:u=a.ops.pop(),a.trys.pop();continue;default:if(!((o=(o=a.trys).length>0&&o[o.length-1])||6!==u[0]&&2!==u[0])){a=0;continue}if(3===u[0]&&(!o||u[1]>o[0]&&u[1]<o[3])){a.label=u[1];break}if(6===u[0]&&a.label<o[1]){a.label=o[1],o=u;break}if(o&&a.label<o[2]){a.label=o[2],a.ops.push(u);break}o[2]&&a.ops.pop(),a.trys.pop();continue}u=n.call(e,a)}catch(e){u=[6,e],r=0}finally{t=o=0}if(5&u[0])throw u[1];return{value:u[0]?u[1]:void 0,done:!0}}([u,c])}}};function i(e,n){return new Promise((function(t){e.addEventListener("message",(function r(o){null!=o.data&&o.data.type===n&&(e.removeEventListener("message",r),t(o.data))}))}))}Object.defineProperty(n,"__esModule",{value:!0}),n.start_workers=n._workers=void 0,i(self,"wasm_bindgen_worker_init").then((function(e){return r(void 0,void 0,void 0,(function(){var n;return o(this,(function(r){switch(r.label){case 0:return[4,Promise.resolve().then((function(){return t(235)}))];case 1:return[4,(n=r.sent()).default(e.module,e.memory)];case 2:return r.sent(),postMessage({type:"wasm_bindgen_worker_ready"}),n.wbg_rayon_start_worker(e.receiver),[2]}}))}))})),n.start_workers=function(e,t,a){return r(this,void 0,void 0,(function(){var u,c=this;return o(this,(function(s){switch(s.label){case 0:if(0===a.num_threads())throw new Error("num_threads must be > 0.");return u={type:"wasm_bindgen_worker_init",module:e,memory:t,receiver:a.receiver()},[4,Promise.all(Array.from({length:a.num_threads()},(function(){return r(c,void 0,void 0,(function(){var e;return o(this,(function(n){switch(n.label){case 0:return(e=new Worker(self.location.href,{type:"module"})).postMessage(u),[4,i(e,"wasm_bindgen_worker_ready")];case 1:return n.sent(),[2,e]}}))}))})))];case 1:return n._workers=s.sent(),a.build(),[2]}}))}))}},925:function(e,n,t){var r=this&&this.__awaiter||function(e,n,t,r){return new(t||(t=Promise))((function(o,i){function a(e){try{c(r.next(e))}catch(e){i(e)}}function u(e){try{c(r.throw(e))}catch(e){i(e)}}function c(e){var n;e.done?o(e.value):(n=e.value,n instanceof t?n:new t((function(e){e(n)}))).then(a,u)}c((r=r.apply(e,n||[])).next())}))},o=this&&this.__generator||function(e,n){var t,r,o,i,a={label:0,sent:function(){if(1&o[0])throw o[1];return o[1]},trys:[],ops:[]};return i={next:u(0),throw:u(1),return:u(2)},"function"==typeof Symbol&&(i[Symbol.iterator]=function(){return this}),i;function u(u){return function(c){return function(u){if(t)throw new TypeError("Generator is already executing.");for(;i&&(i=0,u[0]&&(a=0)),a;)try{if(t=1,r&&(o=2&u[0]?r.return:u[0]?r.throw||((o=r.return)&&o.call(r),0):r.next)&&!(o=o.call(r,u[1])).done)return o;switch(r=0,o&&(u=[2&u[0],o.value]),u[0]){case 0:case 1:o=u;break;case 4:return a.label++,{value:u[1],done:!1};case 5:a.label++,r=u[1],u=[0];continue;case 7:u=a.ops.pop(),a.trys.pop();continue;default:if(!((o=(o=a.trys).length>0&&o[o.length-1])||6!==u[0]&&2!==u[0])){a=0;continue}if(3===u[0]&&(!o||u[1]>o[0]&&u[1]<o[3])){a.label=u[1];break}if(6===u[0]&&a.label<o[1]){a.label=o[1],o=u;break}if(o&&a.label<o[2]){a.label=o[2],a.ops.push(u);break}o[2]&&a.ops.pop(),a.trys.pop();continue}u=n.call(e,a)}catch(e){u=[6,e],r=0}finally{t=o=0}if(5&u[0])throw u[1];return{value:u[0]?u[1]:void 0,done:!0}}([u,c])}}};Object.defineProperty(n,"__esModule",{value:!0}),n.web_index_service_worker=n.WebIndexServiceWorker=n.IndexQuery=void 0;var i=t(375),a=t(235);n.IndexQuery=function(e,n,t){this.index_name=e,this.query=n,this.collectors=t};var u=function(){function e(){}return e.prototype.setup=function(e,n,t){return r(this,void 0,void 0,(function(){return o(this,(function(r){switch(r.label){case 0:return t||(t=function(e,n){return console.log(e,n)}),t("status","setting workers..."),[4,(0,a.default)(e)];case 1:return r.sent(),this.registry=new a.WebIndexRegistry(n>0),n>0?(t("status","setting thread pool of size "+n.toString()+"..."),[4,(0,a.init_thread_pool)(n)]):[3,3];case 2:r.sent(),r.label=3;case 3:return[2]}}))}))},e.prototype.add=function(e){return r(this,void 0,void 0,(function(){return o(this,(function(n){switch(n.label){case 0:return[4,this.registry.add(e)];case 1:return[2,n.sent()]}}))}))},e.prototype.delete=function(e){return r(this,void 0,void 0,(function(){return o(this,(function(n){switch(n.label){case 0:return[4,this.registry.delete(e)];case 1:return[2,n.sent()]}}))}))},e.prototype.search=function(e){return r(this,void 0,void 0,(function(){return o(this,(function(n){switch(n.label){case 0:return[4,this.registry.search(e)];case 1:return[2,n.sent()]}}))}))},e.prototype.cache_metrics=function(){return r(this,void 0,void 0,(function(){return o(this,(function(e){switch(e.label){case 0:return[4,(0,a.cache_metrics)()];case 1:return[2,e.sent()]}}))}))},e.prototype.warmup=function(e){return r(this,void 0,void 0,(function(){return o(this,(function(n){switch(n.label){case 0:return[4,this.registry.warmup(e)];case 1:return[2,n.sent()]}}))}))},e}();n.WebIndexServiceWorker=u,n.web_index_service_worker=new u,i.expose(n.web_index_service_worker)},235:(e,n,t)=>{t.r(n),t.d(n,{WebIndexRegistry:()=>I,cache_metrics:()=>j,default:()=>q,initSync:()=>N,init_thread_pool:()=>M,wbg_rayon_PoolBuilder:()=>W,wbg_rayon_start_worker:()=>O});var r=t(655),o=t(851);let i;e=t.hmd(e);const a=new Array(32).fill(void 0);function u(e){return a[e]}a.push(void 0,null,!0,!1);let c=a.length;function s(e){const n=u(e);return function(e){e<36||(a[e]=c,c=e)}(e),n}function _(e){return null==e}let f=new Float64Array,b=new Int32Array;function l(){return b.buffer!==i.memory.buffer&&(b=new Int32Array(i.memory.buffer)),b}function w(e){c===a.length&&a.push(a.length+1);const n=c;return c=a[n],a[n]=e,n}let d=0,g=new Uint8Array;function p(){return g.buffer!==i.memory.buffer&&(g=new Uint8Array(i.memory.buffer)),g}const y=new TextEncoder("utf-8");function h(e,n,t){if(void 0===t){const t=y.encode(e),r=n(t.length);return p().subarray(r,r+t.length).set(t),d=t.length,r}let r=e.length,o=n(r);const i=p();let a=0;for(;a<r;a++){const n=e.charCodeAt(a);if(n>127)break;i[o+a]=n}if(a!==r){0!==a&&(e=e.slice(a)),o=t(o,r,r=a+3*e.length);const n=function(e,n){const t=y.encode(e);return n.set(t),{read:e.length,written:t.length}}(e,p().subarray(o+a,o+r));a+=n.written}return d=a,o}const m=new TextDecoder("utf-8",{ignoreBOM:!0,fatal:!0});function v(e,n){return m.decode(p().slice(e,e+n))}m.decode();let x=new BigInt64Array;function k(e){const n=typeof e;if("number"==n||"boolean"==n||null==e)return`${e}`;if("string"==n)return`"${e}"`;if("symbol"==n){const n=e.description;return null==n?"Symbol":`Symbol(${n})`}if("function"==n){const n=e.name;return"string"==typeof n&&n.length>0?`Function(${n})`:"Function"}if(Array.isArray(e)){const n=e.length;let t="[";n>0&&(t+=k(e[0]));for(let r=1;r<n;r++)t+=", "+k(e[r]);return t+="]",t}const t=/\[object ([^\]]+)\]/.exec(toString.call(e));let r;if(!(t.length>1))return toString.call(e);if(r=t[1],"Object"==r)try{return"Object("+JSON.stringify(e)+")"}catch(e){return"Object"}return e instanceof Error?`${e.name}: ${e.message}\n${e.stack}`:r}function A(e,n,t,r){const o={a:e,b:n,cnt:1,dtor:t},a=(...e)=>{o.cnt++;const n=o.a;o.a=0;try{return r(n,o.b,...e)}finally{0==--o.cnt?i.__wbindgen_export_3.get(o.dtor)(n,o.b):o.a=n}};return a.original=o,a}function E(e,n,t){i._dyn_core__ops__function__FnMut__A____Output___R_as_wasm_bindgen__closure__WasmClosure___describe__invoke__h8c90d4991c84b4e5(e,n,w(t))}function S(e,n,t){i._dyn_core__ops__function__FnMut__A____Output___R_as_wasm_bindgen__closure__WasmClosure___describe__invoke__h2a0a2411e00c46e3(e,n,w(t))}function j(){return s(i.cache_metrics())}function C(e,n){try{return e.apply(this,n)}catch(e){i.__wbindgen_exn_store(w(e))}}function M(e){return s(i.init_thread_pool(e))}function O(e){i.wbg_rayon_start_worker(e)}function P(e,n){return p().subarray(e/1,e/1+n)}class I{static __wrap(e){const n=Object.create(I.prototype);return n.ptr=e,n}__destroy_into_raw(){const e=this.ptr;return this.ptr=0,e}free(){const e=this.__destroy_into_raw();i.__wbg_webindexregistry_free(e)}constructor(e){const n=i.webindexregistry_new(e);return I.__wrap(n)}search(e){return s(i.webindexregistry_search(this.ptr,w(e)))}add(e){return s(i.webindexregistry_add(this.ptr,w(e)))}get_index_payload(e){const n=h(e,i.__wbindgen_malloc,i.__wbindgen_realloc),t=d;return s(i.webindexregistry_get_index_payload(this.ptr,n,t))}delete(e){const n=h(e,i.__wbindgen_malloc,i.__wbindgen_realloc),t=d;return s(i.webindexregistry_delete(this.ptr,n,t))}warmup(e){const n=h(e,i.__wbindgen_malloc,i.__wbindgen_realloc),t=d;return s(i.webindexregistry_warmup(this.ptr,n,t))}}class W{static __wrap(e){const n=Object.create(W.prototype);return n.ptr=e,n}__destroy_into_raw(){const e=this.ptr;return this.ptr=0,e}free(){const e=this.__destroy_into_raw();i.__wbg_wbg_rayon_poolbuilder_free(e)}num_threads(){return i.wbg_rayon_poolbuilder_num_threads(this.ptr)>>>0}receiver(){return i.wbg_rayon_poolbuilder_receiver(this.ptr)}build(){i.wbg_rayon_poolbuilder_build(this.ptr)}}function R(){const n={wbg:{}};return n.wbg.__wbindgen_object_drop_ref=function(e){s(e)},n.wbg.__wbindgen_is_undefined=function(e){return void 0===u(e)},n.wbg.__wbindgen_in=function(e,n){return u(e)in u(n)},n.wbg.__wbindgen_number_get=function(e,n){const t=u(n),r="number"==typeof t?t:void 0;(f.buffer!==i.memory.buffer&&(f=new Float64Array(i.memory.buffer)),f)[e/8+1]=_(r)?0:r,l()[e/4+0]=!_(r)},n.wbg.__wbindgen_is_bigint=function(e){return"bigint"==typeof u(e)},n.wbg.__wbindgen_bigint_from_u64=function(e){return w(BigInt.asUintN(64,e))},n.wbg.__wbindgen_jsval_eq=function(e,n){return u(e)===u(n)},n.wbg.__wbindgen_boolean_get=function(e){const n=u(e);return"boolean"==typeof n?n?1:0:2},n.wbg.__wbindgen_is_string=function(e){return"string"==typeof u(e)},n.wbg.__wbindgen_string_get=function(e,n){const t=u(n),r="string"==typeof t?t:void 0;var o=_(r)?0:h(r,i.__wbindgen_malloc,i.__wbindgen_realloc),a=d;l()[e/4+1]=a,l()[e/4+0]=o},n.wbg.__wbindgen_is_object=function(e){const n=u(e);return"object"==typeof n&&null!==n},n.wbg.__wbindgen_string_new=function(e,n){return w(v(e,n))},n.wbg.__wbindgen_error_new=function(e,n){return w(new Error(v(e,n)))},n.wbg.__wbg_request_3997f350e483a316=function(){return C((function(e,n,t,o,a){try{return w((0,r.WY)(v(e,n),v(t,o),s(a)))}finally{i.__wbindgen_free(e,n),i.__wbindgen_free(t,o)}}),arguments)},n.wbg.__wbg_startworkers_dd6f4742b1c1ddce=function(e,n,t){return w((0,o.start_workers)(s(e),s(n),W.__wrap(t)))},n.wbg.__wbg_requestasync_082d0cff3efb8ff2=function(){return C((function(e,n,t,o,a){try{return w((0,r.I0)(v(e,n),v(t,o),s(a)))}finally{i.__wbindgen_free(e,n),i.__wbindgen_free(t,o)}}),arguments)},n.wbg.__wbg_new_abda76e883ba8a5f=function(){return w(new Error)},n.wbg.__wbg_stack_658279fe44541cf6=function(e,n){const t=h(u(n).stack,i.__wbindgen_malloc,i.__wbindgen_realloc),r=d;l()[e/4+1]=r,l()[e/4+0]=t},n.wbg.__wbg_error_f851667af71bcfc6=function(e,n){try{console.error(v(e,n))}finally{i.__wbindgen_free(e,n)}},n.wbg.__wbindgen_bigint_from_i64=function(e){return w(e)},n.wbg.__wbindgen_number_new=function(e){return w(e)},n.wbg.__wbindgen_object_clone_ref=function(e){return w(u(e))},n.wbg.__wbindgen_jsval_loose_eq=function(e,n){return u(e)==u(n)},n.wbg.__wbg_getwithrefkey_15c62c2b8546208d=function(e,n){return w(u(e)[u(n)])},n.wbg.__wbg_set_20cbc34131e76824=function(e,n,t){u(e)[s(n)]=s(t)},n.wbg.__wbg_waitAsync_f19aafe62bce576e=function(){return w(Atomics.waitAsync)},n.wbg.__wbg_waitAsync_3c50689953b91515=function(e,n,t){return w(Atomics.waitAsync(u(e),n,t))},n.wbg.__wbg_async_793227563870e13b=function(e){return u(e).async},n.wbg.__wbg_value_9ed8b52e0a7b4e58=function(e){return w(u(e).value)},n.wbg.__wbindgen_cb_drop=function(e){const n=s(e).original;return 1==n.cnt--&&(n.a=0,!0)},n.wbg.__wbg_setonmessage_a31c8547d106bb01=function(e,n){u(e).onmessage=u(n)},n.wbg.__wbg_new_27ec94f7d0136de2=function(){return C((function(e,n){return w(new Worker(v(e,n)))}),arguments)},n.wbg.__wbg_postMessage_8a8f33d997e17e7b=function(){return C((function(e,n){u(e).postMessage(u(n))}),arguments)},n.wbg.__wbg_data_7b1f01f4e6a64fbe=function(e){return w(u(e).data)},n.wbg.__wbg_randomFillSync_6894564c2c334c42=function(){return C((function(e,n,t){u(e).randomFillSync(P(n,t))}),arguments)},n.wbg.__wbg_getRandomValues_805f1c3d65988a5a=function(){return C((function(e,n){u(e).getRandomValues(u(n))}),arguments)},n.wbg.__wbg_crypto_e1d53a1d73fb10b8=function(e){return w(u(e).crypto)},n.wbg.__wbg_process_038c26bf42b093f8=function(e){return w(u(e).process)},n.wbg.__wbg_versions_ab37218d2f0b24a8=function(e){return w(u(e).versions)},n.wbg.__wbg_node_080f4b19d15bc1fe=function(e){return w(u(e).node)},n.wbg.__wbg_require_78a3dcfbdba9cbce=function(){return C((function(){return w(e.require)}),arguments)},n.wbg.__wbg_msCrypto_6e7d3e1f92610cbb=function(e){return w(u(e).msCrypto)},n.wbg.__wbg_get_57245cc7d7c7619d=function(e,n){return w(u(e)[n>>>0])},n.wbg.__wbg_length_6e3bbe7c8bd4dbd8=function(e){return u(e).length},n.wbg.__wbg_new_1d9a920c6bfc44a8=function(){return w(new Array)},n.wbg.__wbindgen_is_function=function(e){return"function"==typeof u(e)},n.wbg.__wbg_newnoargs_b5b063fc6c2f0376=function(e,n){return w(new Function(v(e,n)))},n.wbg.__wbg_new_268f7b7dd3430798=function(){return w(new Map)},n.wbg.__wbg_next_579e583d33566a86=function(e){return w(u(e).next)},n.wbg.__wbg_next_aaef7c8aa5e212ac=function(){return C((function(e){return w(u(e).next())}),arguments)},n.wbg.__wbg_done_1b73b0672e15f234=function(e){return u(e).done},n.wbg.__wbg_value_1ccc36bc03462d71=function(e){return w(u(e).value)},n.wbg.__wbg_iterator_6f9d4f28845f426c=function(){return w(Symbol.iterator)},n.wbg.__wbg_get_765201544a2b6869=function(){return C((function(e,n){return w(Reflect.get(u(e),u(n)))}),arguments)},n.wbg.__wbg_call_97ae9d8645dc388b=function(){return C((function(e,n){return w(u(e).call(u(n)))}),arguments)},n.wbg.__wbg_new_0b9bfdd97583284e=function(){return w(new Object)},n.wbg.__wbg_self_6d479506f72c6a71=function(){return C((function(){return w(self.self)}),arguments)},n.wbg.__wbg_window_f2557cc78490aceb=function(){return C((function(){return w(window.window)}),arguments)},n.wbg.__wbg_globalThis_7f206bda628d5286=function(){return C((function(){return w(globalThis.globalThis)}),arguments)},n.wbg.__wbg_global_ba75c50d1cf384f4=function(){return C((function(){return w(t.g.global)}),arguments)},n.wbg.__wbg_encodeURIComponent_e7f444348deb4645=function(e,n){return w(encodeURIComponent(v(e,n)))},n.wbg.__wbg_set_a68214f35c417fa9=function(e,n,t){u(e)[n>>>0]=s(t)},n.wbg.__wbg_isArray_27c46c67f498e15d=function(e){return Array.isArray(u(e))},n.wbg.__wbg_of_22ee6ea02403744c=function(e,n,t){return w(Array.of(u(e),u(n),u(t)))},n.wbg.__wbg_instanceof_ArrayBuffer_e5e48f4762c5610b=function(e){let n;try{n=u(e)instanceof ArrayBuffer}catch{n=!1}return n},n.wbg.__wbg_call_168da88779e35f61=function(){return C((function(e,n,t){return w(u(e).call(u(n),u(t)))}),arguments)},n.wbg.__wbg_set_933729cf5b66ac11=function(e,n,t){return w(u(e).set(u(n),u(t)))},n.wbg.__wbg_isSafeInteger_dfa0593e8d7ac35a=function(e){return Number.isSafeInteger(u(e))},n.wbg.__wbg_now_58886682b7e790d7=function(){return Date.now()},n.wbg.__wbg_entries_65a76a413fc91037=function(e){return w(Object.entries(u(e)))},n.wbg.__wbg_new_9962f939219f1820=function(e,n){try{var t={a:e,b:n};const r=new Promise(((e,n)=>{const r=t.a;t.a=0;try{return function(e,n,t,r){i.wasm_bindgen__convert__closures__invoke2_mut__h89893cb8c78d6bcd(e,n,w(t),w(r))}(r,t.b,e,n)}finally{t.a=r}}));return w(r)}finally{t.a=t.b=0}},n.wbg.__wbg_resolve_99fe17964f31ffc0=function(e){return w(Promise.resolve(u(e)))},n.wbg.__wbg_then_11f7a54d67b4bfad=function(e,n){return w(u(e).then(u(n)))},n.wbg.__wbg_then_cedad20fbbd9418a=function(e,n,t){return w(u(e).then(u(n),u(t)))},n.wbg.__wbg_buffer_3f3d764d4747d564=function(e){return w(u(e).buffer)},n.wbg.__wbg_new_ea9fa4db667c15a1=function(e){return w(new Int32Array(u(e)))},n.wbg.__wbg_new_8c3f0052272a457a=function(e){return w(new Uint8Array(u(e)))},n.wbg.__wbg_set_83db9690f9353e79=function(e,n,t){u(e).set(u(n),t>>>0)},n.wbg.__wbg_length_9e1ae1900cb0fbd5=function(e){return u(e).length},n.wbg.__wbg_instanceof_Uint8Array_971eeda69eb75003=function(e){let n;try{n=u(e)instanceof Uint8Array}catch{n=!1}return n},n.wbg.__wbg_newwithlength_f5933855e4f48a19=function(e){return w(new Uint8Array(e>>>0))},n.wbg.__wbg_subarray_58ad4efbb5bcb886=function(e,n,t){return w(u(e).subarray(n>>>0,t>>>0))},n.wbg.__wbindgen_bigint_get_as_i64=function(e,n){const t=u(n),r="bigint"==typeof t?t:void 0;(x.buffer!==i.memory.buffer&&(x=new BigInt64Array(i.memory.buffer)),x)[e/8+1]=_(r)?0n:r,l()[e/4+0]=!_(r)},n.wbg.__wbindgen_debug_string=function(e,n){const t=h(k(u(n)),i.__wbindgen_malloc,i.__wbindgen_realloc),r=d;l()[e/4+1]=r,l()[e/4+0]=t},n.wbg.__wbindgen_throw=function(e,n){throw new Error(v(e,n))},n.wbg.__wbindgen_rethrow=function(e){throw s(e)},n.wbg.__wbindgen_module=function(){return w(U.__wbindgen_wasm_module)},n.wbg.__wbindgen_memory=function(){return w(i.memory)},n.wbg.__wbindgen_closure_wrapper1362=function(e,n,t){return w(A(e,n,323,E))},n.wbg.__wbindgen_closure_wrapper1365=function(e,n,t){return w(A(e,n,323,S))},n}function T(e,n){e.wbg.memory=n||new WebAssembly.Memory({initial:27,maximum:16384,shared:!0})}function L(e,n){return i=e.exports,U.__wbindgen_wasm_module=n,x=new BigInt64Array,f=new Float64Array,b=new Int32Array,g=new Uint8Array,i.__wbindgen_start(),i}function N(e,n){const t=R();return T(t,n),e instanceof WebAssembly.Module||(e=new WebAssembly.Module(e)),L(new WebAssembly.Instance(e,t),e)}async function U(e,n){void 0===e&&(e=new URL(t(275),t.b));const r=R();("string"==typeof e||"function"==typeof Request&&e instanceof Request||"function"==typeof URL&&e instanceof URL)&&(e=fetch(e)),T(r,n);const{instance:o,module:i}=await async function(e,n){if("function"==typeof Response&&e instanceof Response){if("function"==typeof WebAssembly.instantiateStreaming)try{return await WebAssembly.instantiateStreaming(e,n)}catch(n){if("application/wasm"==e.headers.get("Content-Type"))throw n;console.warn("`WebAssembly.instantiateStreaming` failed because your server does not serve wasm with `application/wasm` MIME type. Falling back to `WebAssembly.instantiate` which is slower. Original error:\n",n)}const t=await e.arrayBuffer();return await WebAssembly.instantiate(t,n)}{const t=await WebAssembly.instantiate(e,n);return t instanceof WebAssembly.Instance?{instance:t,module:e}:t}}(await e,r);return L(o,i)}const q=U},275:(e,n,t)=>{e.exports=t.p+"index_bg.wasm"},375:(e,n,t)=>{t.r(n),t.d(n,{createEndpoint:()=>o,expose:()=>s,proxy:()=>p,proxyMarker:()=>r,releaseProxy:()=>i,transfer:()=>g,transferHandlers:()=>c,windowEndpoint:()=>y,wrap:()=>f});const r=Symbol("Comlink.proxy"),o=Symbol("Comlink.endpoint"),i=Symbol("Comlink.releaseProxy"),a=Symbol("Comlink.thrown"),u=e=>"object"==typeof e&&null!==e||"function"==typeof e,c=new Map([["proxy",{canHandle:e=>u(e)&&e[r],serialize(e){const{port1:n,port2:t}=new MessageChannel;return s(e,n),[t,[t]]},deserialize:e=>(e.start(),f(e))}],["throw",{canHandle:e=>u(e)&&a in e,serialize({value:e}){let n;return n=e instanceof Error?{isError:!0,value:{message:e.message,name:e.name,stack:e.stack}}:{isError:!1,value:e},[n,[]]},deserialize(e){if(e.isError)throw Object.assign(new Error(e.value.message),e.value);throw e.value}}]]);function s(e,n=self){n.addEventListener("message",(function t(r){if(!r||!r.data)return;const{id:o,type:i,path:u}=Object.assign({path:[]},r.data),c=(r.data.argumentList||[]).map(m);let f;try{const n=u.slice(0,-1).reduce(((e,n)=>e[n]),e),t=u.reduce(((e,n)=>e[n]),e);switch(i){case"GET":f=t;break;case"SET":n[u.slice(-1)[0]]=m(r.data.value),f=!0;break;case"APPLY":f=t.apply(n,c);break;case"CONSTRUCT":f=p(new t(...c));break;case"ENDPOINT":{const{port1:n,port2:t}=new MessageChannel;s(e,t),f=g(n,[n])}break;case"RELEASE":f=void 0;break;default:return}}catch(e){f={value:e,[a]:0}}Promise.resolve(f).catch((e=>({value:e,[a]:0}))).then((e=>{const[r,a]=h(e);n.postMessage(Object.assign(Object.assign({},r),{id:o}),a),"RELEASE"===i&&(n.removeEventListener("message",t),_(n))}))})),n.start&&n.start()}function _(e){(function(e){return"MessagePort"===e.constructor.name})(e)&&e.close()}function f(e,n){return l(e,[],n)}function b(e){if(e)throw new Error("Proxy has been released and is not useable")}function l(e,n=[],t=function(){}){let r=!1;const a=new Proxy(t,{get(t,o){if(b(r),o===i)return()=>v(e,{type:"RELEASE",path:n.map((e=>e.toString()))}).then((()=>{_(e),r=!0}));if("then"===o){if(0===n.length)return{then:()=>a};const t=v(e,{type:"GET",path:n.map((e=>e.toString()))}).then(m);return t.then.bind(t)}return l(e,[...n,o])},set(t,o,i){b(r);const[a,u]=h(i);return v(e,{type:"SET",path:[...n,o].map((e=>e.toString())),value:a},u).then(m)},apply(t,i,a){b(r);const u=n[n.length-1];if(u===o)return v(e,{type:"ENDPOINT"}).then(m);if("bind"===u)return l(e,n.slice(0,-1));const[c,s]=w(a);return v(e,{type:"APPLY",path:n.map((e=>e.toString())),argumentList:c},s).then(m)},construct(t,o){b(r);const[i,a]=w(o);return v(e,{type:"CONSTRUCT",path:n.map((e=>e.toString())),argumentList:i},a).then(m)}});return a}function w(e){const n=e.map(h);return[n.map((e=>e[0])),(t=n.map((e=>e[1])),Array.prototype.concat.apply([],t))];var t}const d=new WeakMap;function g(e,n){return d.set(e,n),e}function p(e){return Object.assign(e,{[r]:!0})}function y(e,n=self,t="*"){return{postMessage:(n,r)=>e.postMessage(n,t,r),addEventListener:n.addEventListener.bind(n),removeEventListener:n.removeEventListener.bind(n)}}function h(e){for(const[n,t]of c)if(t.canHandle(e)){const[r,o]=t.serialize(e);return[{type:"HANDLER",name:n,value:r},o]}return[{type:"RAW",value:e},d.get(e)||[]]}function m(e){switch(e.type){case"HANDLER":return c.get(e.name).deserialize(e.value);case"RAW":return e.value}}function v(e,n,t){return new Promise((r=>{const o=new Array(4).fill(0).map((()=>Math.floor(Math.random()*Number.MAX_SAFE_INTEGER).toString(16))).join("-");e.addEventListener("message",(function n(t){t.data&&t.data.id&&t.data.id===o&&(e.removeEventListener("message",n),r(t.data))})),e.start&&e.start(),e.postMessage(Object.assign({id:o},n),t)}))}}},n={};function t(r){var o=n[r];if(void 0!==o)return o.exports;var i=n[r]={id:r,loaded:!1,exports:{}};return e[r].call(i.exports,i,i.exports,t),i.loaded=!0,i.exports}t.m=e,t.n=e=>{var n=e&&e.__esModule?()=>e.default:()=>e;return t.d(n,{a:n}),n},t.d=(e,n)=>{for(var r in n)t.o(n,r)&&!t.o(e,r)&&Object.defineProperty(e,r,{enumerable:!0,get:n[r]})},t.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),t.hmd=e=>((e=Object.create(e)).children||(e.children=[]),Object.defineProperty(e,"exports",{enumerable:!0,set:()=>{throw new Error("ES Modules may not assign module.exports or exports.*, Use ESM export syntax, instead: "+e.id)}}),e),t.o=(e,n)=>Object.prototype.hasOwnProperty.call(e,n),t.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},(()=>{var e;t.g.importScripts&&(e=t.g.location+"");var n=t.g.document;if(!e&&n&&(n.currentScript&&(e=n.currentScript.src),!e)){var r=n.getElementsByTagName("script");r.length&&(e=r[r.length-1].src)}if(!e)throw new Error("Automatic publicPath is not supported in this browser");e=e.replace(/#.*$/,"").replace(/\?.*$/,"").replace(/\/[^\/]+$/,"/"),t.p=e})(),t.b=document.baseURI||self.location.href;var r={};return(()=>{var e=r;Object.defineProperty(e,"__esModule",{value:!0}),e.NetworkConfig=e.ChunkedCacheConfig=e.WebIndexServiceWorker=e.IndexQuery=e.init=void 0;var n=t(235);e.init=n.default;var o=t(925);Object.defineProperty(e,"IndexQuery",{enumerable:!0,get:function(){return o.IndexQuery}}),Object.defineProperty(e,"WebIndexServiceWorker",{enumerable:!0,get:function(){return o.WebIndexServiceWorker}});var i=t(1);Object.defineProperty(e,"ChunkedCacheConfig",{enumerable:!0,get:function(){return i.ChunkedCacheConfig}}),Object.defineProperty(e,"NetworkConfig",{enumerable:!0,get:function(){return i.NetworkConfig}})})(),r})()));