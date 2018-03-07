## `JSON`如下：
```
{
    "intentions":[
        {
            "name":"call",
            "attributes":[
                {
                    "phoneNumber":[
                        "软终端"
                    ],
                    "dialMode":[
                        "手机"
                    ],
                    "name":[
                        "胡仁林"
                    ]
                }
            ],
            "confidence":1
        }
    ],
    "slotsOption":{
        "sys.name":[
            {
                "oriText":"胡仁林",
                "standardName":"胡仁林",
                "origin":"1520318556915",
                "type":"nr",
                "charOffset":13
            }
        ]
    },
    "code":0,
    "message":"成功"
}
```
## 需求如下:
- 将上述json转成一个对象，可以使用fastjson、Gson等。
- 其中attributes字段里的phoneNumber、dialMode、name是动态变化，也就是不同的json例子这里都会变化，因此我想用一个Map<String, List<Object>>来封装attributes.(注意attributes是一个jsonarray，因此里面的每一个attribute都转成对应的一个map)
- 以上。
