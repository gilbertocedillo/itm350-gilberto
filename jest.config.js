module.exports = {
    coverageThreshold: {
      './src/*.js': {
        lines: 80
      }
    },
    testMatch: ['**/__tests__/**/*.js?(x)', '**/?(*.)+(spec|test).[tj]s?(x)'],
    collectCoverageFrom: ['src/**/*.js']
  }
  