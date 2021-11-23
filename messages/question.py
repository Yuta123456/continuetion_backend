message = {
    "type": "carousel",
    "contents": [
        {
            "type": "bubble",
            "size": "micro",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "達成！",
                        "color": "#ffffff",
                        "align": "start",
                        "size": "md",
                        "gravity": "center"
                    }
                ],
                "backgroundColor": "#DC143C",
                "paddingTop": "19px",
                "paddingAll": "12px",
                "paddingBottom": "16px"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                          {
                              "type": "text",
                              "text": "はい。継続できました！",
                              "size": "xs"
                          }
                        ]
                    }
                ],
                "spacing": "md",
                "paddingAll": "12px"
            },
            "action": {
                "type": "message",
                "label": "action",
                "text": "Yes"
            },
            "styles": {
                "footer": {
                    "separator": false
                }
            }
        },
        {
            "type": "bubble",
            "size": "micro",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "失敗",
                        "color": "#ffffff",
                        "align": "start",
                        "size": "md",
                        "gravity": "center"
                    }
                ],
                "backgroundColor": "#4682B4",
                "paddingTop": "19px",
                "paddingAll": "12px",
                "paddingBottom": "16px"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                          {
                              "type": "text",
                              "text": "明日は頑張ります！",
                              "size": "sm",
                              "wrap": true
                          }
                        ],
                        "flex": 1
                    }
                ],
                "spacing": "md",
                "paddingAll": "12px"
            },
            "action": {
                "type": "message",
                "label": "action",
                "text": "No"
            },
            "styles": {
                "footer": {
                    "separator": false
                }
            }
        }
    ]
}
