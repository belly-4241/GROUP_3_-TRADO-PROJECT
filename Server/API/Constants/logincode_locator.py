

class Logincode():
    URL_Logincode = "https://qa-api.trado.co.il/api/admin-user/logincode"
    Valid_data = {"phone":"1952222222","info":{"lng":"hebrew","getTypes":'false',"platform":"admin","isMobile":
                'false',"screenHeight":864,"screenWidth":1536,"location":{"ancestorOrigins":{},"href":
                "https://qa-admin.trado.co.il/#/login","origin":"https://qa-admin.trado.co.il","protocol":"https:",
                "host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}
    Invalid_logincode = {"phone":"195223332","info":{"lng":"hebrew","getTypes":'false',"platform":"admin","isMobile":
                    'false',"screenHeight":864,"screenWidth":1536,"location":{"ancestorOrigins":{},"href":
                    "https://qa-admin.trado.co.il/#/login","origin":"https://qa-admin.trado.co.il","protocol":"https:",
                    "host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}
    Empty_logincode = {"phone":"","info":{"lng":"hebrew","getTypes":'false',"platform":"admin","isMobile":
                'false',"screenHeight":864,"screenWidth":1536,"location":{"ancestorOrigins":{},"href":
                "https://qa-admin.trado.co.il/#/login","origin":"https://qa-admin.trado.co.il","protocol":"https:",
                "host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}