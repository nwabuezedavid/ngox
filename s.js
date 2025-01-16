setInterval(() => {
    

    fetch("https://api.true.world/api/game/roll", {
        "headers": {
          "accept": "application/json, text/plain, */*",
          "accept-language": "en-US,en;q=0.9,pt;q=0.8",
          "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NzU3NDgzMjM3NCwiZmlyc3ROYW1lIjoiTWljaGFlbCIsImxhc3ROYW1lIjoi8J-QviBKSiBlIiwidXNlcm5hbWUiOiJNaWNoYWVsd2RiYiIsImlhdCI6MTczMzcyOTM1NSwiZXhwIjoxNzMzNzU4MTU1fQ.YXsMT07-dGR7pTrmzABFgdkbdkDeR_heqnh9ihOCu9E",
          "cache": "no-store",
          "downlink": "1.3",
          "if-none-match": "W/\"129-91G8PE6fEyqPXcDWRlTM5gHjva8\"",
          "multiply": "1",
          "priority": "u=1, i",
          "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
          "sec-ch-ua-mobile": "?0",
          "sec-ch-ua-platform": "\"Windows\"",
          "sec-fetch-dest": "empty",
          "sec-fetch-mode": "cors",
          "sec-fetch-site": "same-site",
          "sendtime": "2024-12-09T07:44:20Z",
          "world": "1"
        },
        "referrer": "https://bot.true.world/",
        "referrerPolicy": "strict-origin-when-cross-origin",
        "body": null,
        "method": "GET",
        "mode": "cors",
        "credentials": "include"
      })
.then(e=>e.json())
  .then((result) => {
    console.log(result);
    
  }).catch((err) => {
    console.log(err);
    
  })

}, 2000);