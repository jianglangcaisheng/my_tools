import numpy as np
from matplotlib import pyplot as plt

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


class ToolDraw:
    auxiliary_line_attributes = 'r--'
    font_color = 'r'

    num_figure = 0
    cur_subplot = 1

    def __init__(self, name="", subplot=(1, 1)):
        ToolDraw.num_figure += 1
        self.figure_id = ToolDraw.num_figure
        self.name = name
        self.subplot = subplot

    def draw_data(self, dates, ends, name, stock_check_config,
                  x_left=0, color=(0.5, 0.5, 0.5)):

        if self.cur_subplot == 1:
            fig = plt.figure(self.figure_id, figsize=(19.0, 9.0))
            fig.canvas.set_window_title(self.name)

        ax = plt.subplot(self.subplot[0], self.subplot[1], self.cur_subplot)

        x_length = dates.__len__()

        # draw basic
        if 1:
            x = np.arange(x_length) + x_left
            y = np.array(ends) / 100.0
            if self.cur_subplot == 1:
                plt.title(self.name, fontsize=18)
            else:
                plt.xlabel("日期", fontsize=18)
            plt.ylabel("收盘价", fontsize=18)
            plt.plot(x, y, color=color, label=name)

            if self.cur_subplot == 2:
                plt.legend(fontsize=20)

        # ticklabel
        if 1:
            num = 35
            r = x_length // num

            if r == 0:
                import mine.t_exception as my_exception
                raise my_exception.MyException("data is null")
            xx = np.arange(0, num * r, r)

            date_selected = []
            for i in range(num):
                date_selected.append(dates[r * i].strftime("%y%m"))

            _ = plt.xticks(xx, date_selected, rotation=0)

        # extra draw
        if 1:

            def draw_line(x1, y1, x2, y2, x_vanished=None):
                num_point = 300
                if x_vanished is None:
                    x = np.linspace(x1, x2, num_point)
                    y = np.linspace(y1, y2, num_point)
                else:
                    y_vanished = ((y2 - y1) / (x2 - x1)) * (x_vanished - x1) + y1
                    x = np.linspace(x1, x_vanished, num_point)
                    y = np.linspace(y1, y_vanished, num_point)
                plt.plot(x, y, self.auxiliary_line_attributes)

            def draw_vertical_line(x, y_min, y_max, text):

                plt.text(x, round(y_max * 2 / 3), text, fontsize=10, color=self.font_color)

                num_point = 300
                x = np.array([x] * num_point)
                y = np.linspace(y_min, y_max, num_point)
                plt.plot(x, y, self.auxiliary_line_attributes)

            def find_x(date, dates):
                for i in range(x_length):
                    if (dates[i] - date).days >= 0:
                        return i

            if stock_check_config.__contains__("lines"):
                draw_lines = stock_check_config["lines"]
                for draw_data in draw_lines:
                    draw_date = draw_data[0]

                    for i in range(x_length):
                        if draw_date == dates[i]:
                            draw_vertical_line(i, np.min(y), y[i], draw_date.strftime("%y%m%d"))
                            break

            if stock_check_config.__contains__("slash"):
                draw_slash = stock_check_config["slash"]
                for draw_data in draw_slash:
                    draw_date1 = draw_data[0]
                    y1 = draw_data[1] / 100.0
                    draw_date2 = draw_data[2]
                    y2 = draw_data[3] / 100.0

                    x1 = find_x(draw_date1, dates)
                    if x1 <= 0:
                        continue
                    x2 = find_x(draw_date2, dates)
                    draw_line(x1, y1, x2, y2, dates.__len__())
                    plt.plot(x1, y1, 'ro')
                    plt.plot(x2, y2, 'ro')

            if stock_check_config.__contains__("texts") and self.cur_subplot == 1:
                texts = stock_check_config["texts"]
                for text in texts:

                    draw_date = text[0]
                    y_text_rate = text[1]
                    content = text[2]

                    if draw_date is None:
                        plt.text(x_length / 20, round(max(y) * 7 / 10),
                                 content, fontsize=10, color=self.font_color)
                    else:
                        for i in range(x_length):
                            if (dates[i] - draw_date).days >= 0:
                                plt.text(i, round(np.max(y) * y_text_rate), content,
                                         fontsize=10, color=self.font_color)
                                break

            plt.text(x_length, ends[-1] / 100., ends[-1] / 100.,
                     fontsize=10, color=self.font_color)
            x = np.arange(x_length) + x_left
            y = np.ones(x_length) * ends[-1] / 100.0
            plt.plot(x, y, self.auxiliary_line_attributes)

        # show
        if 1:
            plt.margins(0)
            plt.subplots_adjust(bottom=0.06, top=0.95, left=0.04, right=0.98)

    def show(self):

        import mine.t_exception as t_exception
        raise t_exception.MyException("Not pass.")

        # 完全全屏
        if 0:
            plt.get_current_fig_manager().full_screen_toggle()

        plt.show()

    @staticmethod
    def plt_show():
        plt.show()


if __name__ == "__main__":

    plt.figure(1)

    plt.plot([10], [100], 'ro')

    x = np.arange(100)
    y = 2 * x + 5
    plt.title("Matplotlib demo")
    plt.xlabel("x axis caption")
    plt.ylabel("y axis caption")
    plt.plot(x, y)
    index_ls = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', '8', '9', '10']
    _ = plt.xticks(np.arange(0, 100, 10), index_ls)  ## 可以设置坐标字

    if 0:
        val_ls = [np.random.randint(100) + i * 20 for i in range(7)]
        scale_ls = range(7)
        plt.bar(scale_ls, val_ls)
        index_ls = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        _ = plt.xticks(scale_ls, index_ls)  ## 可以设置坐标字

    plt.show()
