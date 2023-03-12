from pyecharts.charts import Bar, Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import *
bar1 = Bar()
bar1.add_xaxis(['中国', "美国", '英国'])
bar1.add_yaxis('GDP', [40, 20, 10], label_opts=LabelOpts(position="right"))
bar1.reversal_axis()
bar2 = Bar()
bar2.add_xaxis(['中国', "美国", '英国'])
bar2.add_yaxis('GDP', [100, 10, 15], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

timeLine = Timeline({
    "theme": ThemeType.MACARONS
})
timeLine.add(bar1, '2021年GDP')
timeLine.add(bar2, '2022年GDP')

# 设置自动播放
timeLine.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)
timeLine.render('基础柱状图时间线.html')

