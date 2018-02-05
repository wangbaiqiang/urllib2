# coding:utf-8
# 爬去数据显示到html中
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    # 收集数据
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    # 收集数据写入到html文件中
    def output_html(self):
        fout = open('output.html', 'w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        # 默认是ascii 中文要改成utf-8
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td> %s </td>" % data['url'])
            fout.write("<td> %s </td>" % data['title']).encoding('utf-8')
            fout.write("<td> %s </td>" % data['summary']).encoding('utf-8')
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
