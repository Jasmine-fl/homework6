#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2

def make_output(input1,input2):
    len1 = len(input1)
    len2 = len(input2)
    output = []
    if len1 == len2:
        for i in range(len1):
            output.append(input1[i])
            output.append(input2[i])
    elif len1 > len2:
        for i in range(len2):
            output.append(input1[i])
            output.append(input2[i])
        output.append(input1[len2:len1])
    else:
        for i in range(len1):
            output.append(input1[i])
            output.append(input2[i])
        output.append(input2[len1:len2])
    output = "".join(output)
    return str(output)

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        input1 = self.request.get("input1")
        input2 = self.request.get("input2")
        output = make_output(input1, input2)
        self.response.write("""
        <!DOCTYPE html>
        <html lang="ja">
        <head>
            <meta charset="UTF-8">
            <title>パタトクカシーー</title>
        </head>
        <body>

        <h1>パタトクカシーー</h1>

        <h3>好きな単語を2つ入力してください</h3>
        <form>
        <p>入力 1つ目の単語(例 パトカー):　<input type="text" name="input1" size="45"></p>

        <p>入力 2つ目の単語(例 タクシー):　<input type="text" name="input2" size="45"></p>

        <p><input type="submit" value="送信"></p>
        </form>
        <br>
        <h3>出力: %s</h3>
        <h4><output type="text" name="output"></h4>

        </body>
        </html>
        """ % output)

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
