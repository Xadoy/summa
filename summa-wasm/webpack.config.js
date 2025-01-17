import path from "path";
import {fileURLToPath} from 'url';
import WasmPackPlugin from '@wasm-tool/wasm-pack-plugin';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

export default {
    entry:  {
        'main': './src/index.ts',
        'worker': './src/web-index-service-worker.ts'
    },
    target: "web",
    output: {
        assetModuleFilename: '[name][ext]',
        clean: true,
        path: path.resolve(__dirname, 'dist'),
        filename: '[name].js',
        library: 'summa-wasm',
        libraryTarget: 'umd',
        umdNamedDefine: true
    },
    experiments: {
        topLevelAwait: true
    },
    module: {
        rules: [
            {
                test: /\.tsx?$/,
                use: 'ts-loader',
                exclude: /node_modules/,
            }
        ],
    },
    resolve: {
        extensions: ['.tsx', '.ts', '.js'],
    },
    plugins: [
        new WasmPackPlugin({
            crateDirectory: path.resolve(__dirname, 'crate'),
            args: '--log-level warn',
            extraArgs: "--target web --mode normal",
            forceMode: "production",
        })
    ]
}