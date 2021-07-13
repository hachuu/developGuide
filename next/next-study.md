# Next 정리 하기

##. Next 구조
1. _document.js

SPA의 시작점 index.html라고 생각하면 됨

2. next.config.js
Next.js의 라우팅 설정을 작성
```
const withLess = require('@zeit/next-less');
const withTypescript = require('@zeit/next-typescript');

// fix: prevents error when .less files are required by node
if (typeof require !== 'undefined') {
    require.extensions['.less'] = file => {}
}

module.exports = withTypescript(withLess({
    lessLoaderOptions: {
        javascriptEnabled: true,
    },
    exportPathMap: () => return {
        '/': { page: '/' },
        '/about': { page: '/about' },
        '/readme.md': { page: '/readme' },
        '/p/hello-nextjs': { page: '/post', query: { title: 'hello-nextjs' } },
        '/p/learn-nextjs': { page: '/post', query: { title: 'learn-nextjs' } },
        '/p/deploy-nextjs': { page: '/post', query: { title: 'deploy-nextjs' } }
    },
}));
```

3. _error.js

Error 처리 공통으로 할 수 있음
