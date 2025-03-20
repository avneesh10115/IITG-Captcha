document.addEventListener('DOMContentLoaded', function() {
    browser.tabs.executeScript({
        code: `var mag = 0;`
    });
    document.getElementById('magic').addEventListener('click', function() {
        browser.tabs.executeScript({
            code: `mag = !mag;`
        });
    });
    document.getElementById('solve').addEventListener('click', function() {
      browser.tabs.executeScript({
        code: `
            var fetchURL = '';
            var ref = '';
            if (window.location.toString() == 'https://online.iitg.ac.in/iitgauth/login.jsp'){
                fetchURL = 'https://online.iitg.ac.in/iitgauth/captchaimage.jsp';
                ref = 'https://online.iitg.ac.in/iitgauth/login.jsp';
            }
            else {
                fetchURL = 'https://online.iitg.ac.in/sso/captchaimage.jsp';
                ref = 'https://online.iitg.ac.in/sso/index.jsp';
            }
            
            if (window.location.toString() != 'https://online.iitg.ac.in/iitgauth/login.jsp' && window.location.toString() != 'https://online.iitg.ac.in/sso/')
                alert('Wrong Page!');
            else{
                var base64String = '';
                var resp = fetch(fetchURL, {
                    "credentials": "include",
                    "headers": {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
                        "Accept": "image/avif,image/webp,*/*",
                        "Accept-Language": "en-US,en;q=0.5",
                        "Sec-Fetch-Dest": "image",
                        "Sec-Fetch-Mode": "no-cors",
                        "Sec-Fetch-Site": "same-origin",
                        "Priority": "u=4",
                        "Pragma": "no-cache",
                        "Cache-Control": "no-cache"
                    },
                    "referrer": ref,
                    "method": "GET",
                    "mode": "cors"
                });
                resp.then(function (val) {
                    var blob = val.blob();
                    blob.then(function (v) {
                        const reader = new FileReader();
                        reader.onload = function(event) {
                            base64String = event.target.result.split(',')[1];
                            console.log('here');
                            if(!mag){
                                document.getElementById('imgCaptcha').setAttribute('src','data:image/jpeg;base64,'.concat(base64String));  
                            }
                            
                            var res =   fetch('http://localhost:5000/run', {
                                method: 'POST',
                                headers: {'content-type': 'application/json'},
                                body: JSON.stringify({ arg: base64String })
                            });
                            var resj = res.then(response =>                             
                                response.json());
                            resj.then(data => {
                                console.log(data.answer);
                                document.getElementById('input_captcha').setAttribute('value',data.answer);
                                document.getElementById('input_captcha').setAttribute('placeholder',data.answer);
                                document.getElementsByClassName('btn btn-primary btn-lg btn-block')[0].click();
                            })
                            .catch(error => console.error('Error:', error));
                        };
                        reader.readAsDataURL(v);
                        
                    });
                }); 
            }
          `,
      });
    });
    document.getElementById('solve').click();
  });