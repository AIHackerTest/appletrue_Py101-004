#### TASK

读取文件weather_info.txt 文件，完成一个最简天气查询程序，运行在命令行界面，实现以下功能：
输入城市名，返回该城市的天气数据；
输入help，打印帮助文档；
输入exit，退出程序的交互
#退出程序之前，打印查询过的所有城市

#### Learning Tips

- 命名的规范性，减少不必要的冲突。如原字典的命名 dict 与内置函数等容易产生冲突，更名为更为好懂的词汇，如 weather_dict{}
- with open..as filename  with..as 会在调用完毕后自动关闭该文件,则不需要再f.close（）设置关闭，也不要在循环过程中遇到此语句使得循环异常终止
- history.update({city:weather_dict[city]})  此处需要区别字典的更新与列表的更新所用方法不同，list.append()
- 设置存储用户输入的历史记录为字典history{},但是应该思考，若用户两次输入同一个城市，进行多次查询，因字典的key：value 的唯一性，则会出现打印记录不全的情况，应选择list[]  数据结构最佳
- split()/strip()/lstrip()/rstrip() 等切片需要掌握
- 最小化调试，程序出现报错时，应该根据提示的错误类型，先定位错误或问题类型，方向不能错，否则南辕北辙；尝试解决时，最小的单位，步步print，才能不步步惊心，送来的才是步步解密的过程，GET！
- 注意人机交互的用户体验，工作当中经常提倡用户体验提倡细节，这里没有形成很好的迁移，想象对面坐着为一小白，如何使其参与其中，并在机器的提示指引下完成程序的验收，速速的迁移学习技能，GET！

- 实现思路的flow
![weather_search](https://github.com/appletrue/Py101-004/blob/master/Chap1/project/170815.jpg)
