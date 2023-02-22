class Login_API:
    url_login = 'https://qa-api.trado.co.il/api/admin-user/login'
    Valid_data = {"phone":"1952222222","code":"1234","rememberMe":'true',"info":{"lng":"hebrew",
                "getTypes":'false',"platform":"admin","isMobile":'false',"screenHeight":864,"screenWidth":1536,
                "location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":
                "https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":
                "qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}
    Invalid_phone = {"phone":"1952342222","code":"1234","rememberMe":'true',"info":{"lng":"hebrew",
                "getTypes":'false',"platform":"admin","isMobile":'false',"screenHeight":864,"screenWidth":1536,
                "location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":
                "https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":
                "qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}
    Invalid_code = {"phone":"1952222222","code":"2334","rememberMe":'true',"info":{"lng":"hebrew",
                "getTypes":'false',"platform":"admin","isMobile":'false',"screenHeight":864,"screenWidth":1536,
                "location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":
                "https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":
                "qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}
    Invalid_remember = {"phone":"1952222222","code":"1234","rememberMe":'false',"info":{"lng":"hebrew",
                "getTypes":'false',"platform":"admin","isMobile":'false',"screenHeight":864,"screenWidth":1536,
                "location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":
                "https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":
                "qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}
    Invalid_phone_code = {"phone":"1952223222","code":"9334","rememberMe":'true',"info":{"lng":"hebrew",
                "getTypes":'false',"platform":"admin","isMobile":'false',"screenHeight":864,"screenWidth":1536,
                "location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":
                "https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":
                "qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}
    Invalid_phone_remember = {"phone":"19522452222","code":"1234","rememberMe":'false',"info":{"lng":"hebrew",
                "getTypes":'false',"platform":"admin","isMobile":'false',"screenHeight":864,"screenWidth":1536,
                "location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":
                "https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":
                "qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}
    Invalid_code_remember = {"phone":"1952222222","code":"1634","rememberMe":'false',"info":{"lng":"hebrew",
                "getTypes":'false',"platform":"admin","isMobile":'false',"screenHeight":864,"screenWidth":1536,
                "location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":
                "https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":
                "qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}
    Invalid_data = {"phone":"1952292222","code":"1934","rememberMe":'false',"info":{"lng":"hebrew",
                "getTypes":'false',"platform":"admin","isMobile":'false',"screenHeight":864,"screenWidth":1536,
                "location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":
                "https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":
                "qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}
    Empty_phone = {"phone":"","code":"1234","rememberMe":'true',"info":{"lng":"hebrew",
                "getTypes":'false',"platform":"admin","isMobile":'false',"screenHeight":864,"screenWidth":1536,
                "location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":
                "https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":
                "qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}
    Empty_code = {"phone":"1952222222","code":"","rememberMe":'true',"info":{"lng":"hebrew",
                "getTypes":'false',"platform":"admin","isMobile":'false',"screenHeight":864,"screenWidth":1536,
                "location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":
                "https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":
                "qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}
    Empty_phone_code = {"phone":"","code":"","rememberMe":'true',"info":{"lng":"hebrew",
                "getTypes":'false',"platform":"admin","isMobile":'false',"screenHeight":864,"screenWidth":1536,
                "location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":
                "https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":
                "qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}
    Emtpy_phone_code_invalid_remember = {"phone":"","code":"","rememberMe":'false',"info":{"lng":"hebrew",
                "getTypes":'false',"platform":"admin","isMobile":'false',"screenHeight":864,"screenWidth":1536,
                "location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":
                "https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":
                "qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}