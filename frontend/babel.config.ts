import type { TransformOptions } from '@babel/core';

const config: TransformOptions = {
    presets: [
        ["@babel/preset-env", { targets: { node: "current" } }],
        "@babel/preset-react",
        "@babel/preset-typescript",
      ],
      plugins: ["@babel/plugin-transform-runtime"],
};

export default config;
