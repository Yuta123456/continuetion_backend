question = {
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
                    },
                    {
                        "type": "image",
                        "url": "https://1.bp.blogspot.com/-BI3NLgiXyfU/XhwqHZyyYII/AAAAAAABW8I/LUNmfLwUd1EJlZFx_803EFpzE_-fGnYTACNcBGAsYHQ/s1600/body_finger_ok.png"
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
                    "separator": False
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
                    },
                    {
                        "type": "image",
                        "url": "https://2.bp.blogspot.com/-uibfmd5hM2s/U1T3pOR-DFI/AAAAAAAAfUQ/jnm-FEcHVJg/s800/figure_hand_batsu.png"
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
                              "wrap": True
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
                    "separator": False
                }
            }
        }
    ]
}
