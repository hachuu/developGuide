# 301, 302 Redirection 처리 방법
- 301과 302의 차이
- 301: 영구적
- 302: 임시적
- SEO에는 301이 맞음
```
app.get('/blog|/blog/*', (req, res) => {

  const urlInfo = req.url.replace('/blog', '');
  const urlMapping = getBlogMappedID(urlInfo);
  if (urlMapping) {
    res.writeHead(302, { Location: 'newRedirectUrl/'+urlMapping });
    res.end();
  } else {
    res.render('index', {
      req,
      res
    });
  }
});
```

# import 방식
- app.js에서 require형식으로 가져옴
```
const {getBlogMappedID} = require('./blog.js');
```

- import 되는 파일 형식

```
const getBlogMappedID = (id) => {
  const blog = {
    id: 'mappedId'
  }
  return blog[id]
}

module.exports = {
  getBlogMappedID,
};

```
