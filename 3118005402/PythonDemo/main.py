# 这是一个示例
# Python
# 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 Double Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import argparse
import wx
import os.path

from creation import configuration, construction
from solution import formula_answer, check


def main():
    # 在下面的代码行中使用断点来调试脚本。
    parser = argparse.ArgumentParser(description="***** this is auto-generate-expression *****")
    parser.add_argument("-n", metavar="--number", dest="formula_num_arg", help="Generate a given number of expressions")
    parser.add_argument("-r", metavar="--range", dest="range_arg", help="Specify the range of operands")
    parser.add_argument("-e", metavar="--exercise file", dest="exercise_arg",
                        help="Given four arithmetic problem files")
    parser.add_argument("-a", metavar="--answer file", dest="answer_arg",
                        help="Given four arithmetic problem answer files")
    args = parser.parse_args()

    if args.formula_num_arg:
        if args.range_arg:
            config = configuration(formula_num=int(args.formula_num_arg), num_length=int(args.range_arg))
        else:
            config = configuration(formula_num=args.formula_num_arg)
        print('**** 程序正在生成满足要求的各项表达式 ****')
        building = construction()
        result_list = building.construct(config)
        building.formula_output(result_list)
        formula_answer(result_list)
        print('**** 所需题目已生成完毕 ****')

    elif args.exercise_arg:
        if args.answer_arg:
            check(args.exercise_arg, args.answer_arg)
        else:
            print('请给出答案文件')
            exit(0)

    else:
        def open_exercise_file(event):  # 定义打开题目文件事件
            exp_path = r'D:\PythonDemo\Exercises.txt'
            with open(exp_path, "r", encoding="utf-8") as f:  # encoding参数是为了在打开文件时将编码转为utf8
                content_text.SetValue(f.read())

        def open_answer_file(event):  # 定义打开答案文件事件
            ans_path = r'D:\PythonDemo\Answer.txt'
            with open(ans_path, "r", encoding='utf-8') as file:
                content_text.SetValue(file.read())

        def open_grade_file(event):  # 定义打开对比结果文件事件
            exp_path = r'D:\PythonDemo\Grade.txt'
            with open(exp_path, "r", encoding="utf-8") as f:  # encoding参数是为了在打开文件时将编码转为utf8
                content_text.SetValue(f.read())

        def get_path(event):  # 定义打开题目文件事件
            user_path = check_path.GetValue()
            if os.path.exists(user_path) is False:
                content_text.SetValue('请再次确认输入路径正确')
            else:
                check(r'D:\PythonDemo\Exercises.txt', user_path)
                content_text.SetValue('对比成功，请点击查看成绩按钮查看')

        def enter_data(event):
            num = num_text.GetValue()
            range_num = range_num_text.GetValue()
            if num:
                config1 = configuration(formula_num=int(num), num_length=int(range_num))
            else:
                config1 = configuration(formula_num=int(num))
            building1 = construction()
            result_list1 = building1.construct(config1)
            building1.formula_output(result_list1)
            formula_answer(result_list1)
            content_text.SetValue('所需题目已生成完毕')

        app = wx.App()
        frame = wx.Frame(None, title="Gui Test ", pos=(1000, 200), size=(500, 400))

        panel = wx.Panel(frame)

        num_text = wx.TextCtrl(panel)
        range_num_text = wx.TextCtrl(panel)
        check_path = wx.TextCtrl(panel)

        Exercises_button = wx.Button(panel, label="Exercises.txt")
        Exercises_button.Bind(wx.EVT_BUTTON, open_exercise_file)  # 绑定打开文件事件到open_button按钮上

        Answer_button = wx.Button(panel, label="Answer.txt")
        Answer_button.Bind(wx.EVT_BUTTON, open_answer_file)

        Enter_button = wx.Button(panel, label="确认")
        Enter_button.Bind(wx.EVT_BUTTON, enter_data)

        Enter_path_button = wx.Button(panel, label="确认输入框里的存放答案的txt文件的地址正确")
        Enter_path_button.Bind(wx.EVT_BUTTON, get_path)

        Grade_button = wx.Button(panel, label="查看成绩")
        Grade_button.Bind(wx.EVT_BUTTON, open_grade_file)

        content_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        #  wx.TE_MULTILINE可以实现以滚动条方式多行显示文本,若不加此功能文本文档显示为一行

        hezi = wx.BoxSizer()  # 不带参数表示默认实例化一个水平尺寸器
        # proportion：相对比例
        # flag：填充的样式和方向,wx.EXPAND为完整填充，wx.ALL为填充的方向
        # border：边框
        hezi.Add(num_text, proportion=2, flag=wx.EXPAND | wx.ALL, border=3)  # 添加组件
        hezi.Add(range_num_text, proportion=2, flag=wx.EXPAND | wx.ALL, border=3)  # 添加组件
        hezi.Add(Enter_button, proportion=2, flag=wx.EXPAND | wx.ALL, border=3)  # 添加组件

        answer = wx.BoxSizer()  # 不带参数表示默认实例化一个水平尺寸器
        # proportion：相对比例
        # flag：填充的样式和方向,wx.EXPAND为完整填充，wx.ALL为填充的方向
        # border：边框
        answer.Add(check_path, proportion=2, flag=wx.EXPAND | wx.ALL, border=3)  # 添加组件
        answer.Add(Enter_path_button, proportion=2, flag=wx.EXPAND | wx.ALL, border=3)  # 添加组件

        box = wx.BoxSizer()  # 不带参数表示默认实例化一个水平尺寸器
        # proportion：相对比例
        # flag：填充的样式和方向,wx.EXPAND为完整填充，wx.ALL为填充的方向
        # border：边框Grade
        # box.Add(path_text, proportion=5, flag=wx.EXPAND | wx.ALL, border=3)  # 添加组件
        box.Add(Exercises_button, proportion=2, flag=wx.EXPAND | wx.ALL, border=3)  # 添加组件
        box.Add(Answer_button, proportion=2, flag=wx.EXPAND | wx.ALL, border=3)  # 添加组件
        box.Add(Grade_button, proportion=2, flag=wx.EXPAND | wx.ALL, border=3)  # 添加组件

        v_box = wx.BoxSizer(wx.VERTICAL)  # wx.VERTICAL参数表示实例化一个垂直尺寸器
        v_box.Add(hezi, proportion=1, flag=wx.EXPAND | wx.ALL, border=3)  # 添加组件
        v_box.Add(answer, proportion=1, flag=wx.EXPAND | wx.ALL, border=3)
        v_box.Add(box, proportion=1, flag=wx.EXPAND | wx.ALL, border=3)  # 添加组件
        v_box.Add(content_text, proportion=5, flag=wx.EXPAND | wx.ALL, border=3)  # 添加组件

        panel.SetSizer(v_box)  # 设置主尺寸器

        frame.Show()
        app.MainLoop()


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    main()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
