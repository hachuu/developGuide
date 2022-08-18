1. pdf 다운로드 (jspdf 라이브러리 합쳐서)
```
downPdf() {
    const element = document.getElementById(
      `downloadPdf${고유아이디}`,
    ) as HTMLElement;
    const height = element.offsetHeight;
    const width = element.offsetWidth;
    html2canvas(element, {
      windowHeight: window.outerHeight + window.innerHeight,
      scrollY: -window.scrollY,
      height,
      width,
      useCORS: true,
      background: "#FFFFFF",
    })
      .then(function (canvas: {
        toDataURL: (arg0: string) => any;
        height: number;
        width: number;
      }) {
        let imgData = canvas.toDataURL("image/png");
        let margin = 10;
        let imgWidth = 210 - 10 * 2;
        let pageHeight = imgWidth * 1.414;
        let imgHeight = (canvas.height * imgWidth) / canvas.width;
        let heightLeft = imgHeight;
        let doc = new jsPDF("p", "mm");
        let position = margin;
        doc.addImage(imgData, "PNG", margin, position, imgWidth, imgHeight);

        heightLeft -= pageHeight;
        while (heightLeft >= 20) {
          position = heightLeft - imgHeight;
          doc.addImage(imgData, "PNG", 0, position, imgWidth, imgHeight);
          doc.addPage();
          heightLeft -= pageHeight;
        }
        doc.save("sample.pdf");
      })
      .finally(() => {});
  }
```
2. 이미지 다운로드
```
downThumbnail() {
    
    var shareContent = document.getElementsByClassName(
      "template",
    )[0] as HTMLElement;
    var width = shareContent.offsetWidth;
    var height = shareContent.offsetHeight;
    var canvas = document.createElement("canvas");
    var scale = 2;
    var imgType = "image/jpg";
    canvas.width = width * scale;
    canvas.height = height * scale;
    canvas.getContext("2d")?.scale(scale, scale);

    html2canvas(shareContent, {
      width,
      height, //: window.outerHeight + window.innerHeight,
      windowHeight: window.outerHeight + window.innerHeight,
      scrollY: -window.scrollY,
      useCORS: true,
    }).then(function (canvas: { toDataURL: (arg0: string) => string }) {
      var el = document.createElement("a");
      el.href = canvas.toDataURL("image/jpeg");
      el.download = "이미지_이름.jpg";
      el.click();
    });
  }
```

3. 여러가지 시도들..
```
// html2canvas(document.getElementById("template-box")).then(
    //   (canvas: { toDataURL: (arg0: string) => any }) => {
    //     saveAs(canvas.toDataURL("image/png"), "capture01.png");
    //   },
    // );
    // html2canvas(document.getElementById("template-box")).then(
    //   function (canvas: { toDataURL: () => any }) {
    //     console.log(canvas.toDataURL());

    //     function saveAs(uri: string, filename: string) {
    //       var link = document.createElement("a");
    //       // if (typeof link.download === "string") {
    //       debugger;
    //       link.href = uri;
    //       link.download = filename;

    //       //Firefox requires the link to be in the body
    //       document.body.appendChild(link);

    //       //simulate click
    //       link.click();

    //       //remove the link when done
    //       document.body.removeChild(link);
    //       // } else {
    //       //   window.open(uri);
    //       // }
    //     }

    //     saveAs(canvas.toDataURL(), "_Media.jpg");
    //     // saveAs(canvas.toDataURL("image/png"), "capture01.png");
    //   },
    // );
    
    
    // downThumbnail() {
  //   const element = document.getElementById("template-box") as HTMLElement;

  //   const width = element.offsetWidth; //  dom  （      、      ，      ）
  //   const height = element.offsetHeight;

  //   html2canvas(document.getElementById("template-box"), {
  //     width,
  //     height,
  //     useCORS: true,
  //   }).then(function (canvas: { toDataURL: (arg0: string) => string }) {
  //     // var myImg = canvas.toDataURL("image/png");
  //     // myImg = myImg.replace("data:image/png;base64,", "");
  //     // console.log(myImg);

  //     function dataURItoBlob(dataURI: string) {
  //       //console.log( dataURI.replace(/^data:image\/(png|jpeg);base64,/, ""))
  //       var byteStr = atob(dataURI.split(",")[1]);
  //       var mimeStr = dataURI.split(",")[0].split(":")[1].split(";")[0];

  //       var arrBuf = new ArrayBuffer(byteStr.length);
  //       var uInt8Arr = new Uint8Array(arrBuf);
  //       for (var i = 0; i < byteStr.length; i++) {
  //         uInt8Arr[i] = byteStr.charCodeAt(i);
  //       }
  //       return new Blob([uInt8Arr], { type: mimeStr });
  //     }
  //     var blob = dataURItoBlob(canvas.toDataURL("image/jpeg"));
  //     var objectURL = URL.createObjectURL(blob);

  //     var el = document.createElement("a");

  //     el.href = objectURL;
  //     // el.href = canvas.toDataURL("image/jpeg");
  //     el.download = "이미지.jpg"; //다운로드 할 파일명 설정
  //     el.click();
  //   });
  // }
```
