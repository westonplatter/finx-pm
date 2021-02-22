module.exports = {
    entry: {
        main: "./api/static/js/index.js",
    },
    module: {
        rules: [
            {
                test: /.(js|jsx)$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            },
            {
                test: /\.(svg|png|jpg|jpeg|gif)$/,
                loader: "file-loader",
                options: {
                    name: "[name].[ext]",
                    outputPath: "../../api/static/dist",
                },
            },
            {
                test: /\.css$/i,
                use: ["style-loader", "css-loader"],
            },
            {
              test: /\.(scss)$/,
              use: [
                  {
                      loader: 'style-loader', // inject CSS to page
                  }, {
                      loader: 'css-loader', // translates CSS into CommonJS modules
                  }, {
                      loader: 'postcss-loader', // Run post css actions
                      options: {
                          postcssOptions: {
                              plugins: function () {
                                  return [
                                    require('precss'),
                                    require('autoprefixer')
                                  ];
                                }
                          }
                      }
                  }, {
                      loader: 'sass-loader',
                      options: {
                          sassOptions: {
                              // indentedSyntax: true
                          }
                      }
                  }
              ]
          }
        ]
    },
    output: {
        path: __dirname + "/api/static/dist",
        filename: "[name].bundle.js",
    },

    devtool: "source-map"
};
