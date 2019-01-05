# 两个爬虫项目
## 1 爬取我的CSDN博客信息，包括总访问量、等级、评论数等信息，还有各个文章的具体信息<br>
[我的博客](https://blog.csdn.net/liuchengzimozigreat)<br>
## 2 国科大2017-2019年硕士生的信息，可以用这些信息做一些有趣的事<br>
   我收集的网址：（因为各个网站自身问题，有些可能会遇到打不开的情况）<br>
    [19年推免生网址](https://www.baidu.com/link?url=LryJOw6InOpynDIHL6PiHnxiUfYxLrJ7dzlvR9LNcnegbxQQELsZAFvekXlVQxwoMSBNryM6xS_HWbz0f8gQANW07J3bfIAMyZsPzm_vyuzj7p0xi2pQbpgiXXXRTt03zytEmEqsVEau0ZnB2jUjLTNDZtlqMABnga-lWWfwUDArnArKR2fdw8txOcICbrQ6&wd=&eqid=f2428bfe0004d4e6000000065c2b0b7b)<br>
    [18年推免生网址](http://admission.ucas.ac.cn/showarticle/article/4c7e0e9f-2311-47a0-8f12-b0ec992078ac/26651774-b9eb-4399-9b44-3acbc90e2d34)<br>
    [19推免](https://www.baidu.com/link?url=9WXlXdkuoyw_dp5gtynfkeDsebs8gzgL-KmYqqlnzqCZD9j5s-XYaHqFSQhkG0oyAgmTNnX7OOOyVjLtwZuJPuZtjLHBrJE2ExlvqhXm50HzoxI1ItKi0v6yyVaX5VIHPBrksUPH61GwPhkTcVdB3ECkK1iJPw-RQaeC9YehcKbYoFIOeFXJElWJv35-GXSJ&wd=&eqid=adda8e3b00043aec000000065c2b0e32)<br>
    [17年公开招考生网址](http://admission.ucas.edu.cn/showarticle/Article/4c7e0e9f-2311-47a0-8f12-b0ec992078ac/7a5c35a4-0d9d-4918-ac7e-21af8dbd11c3)<br>
    [17推免](https://www.baidu.com/link?url=DUzwlgWDRp0d_nipcI1pOO5AodynyTM6KUunpXybqrl5aP_UVH5DVvuRMOiMJXwSyhFtjc5-rpG5i4rJIiOg228luYqoqJe9GodMEt-4CfK31J_sKuNsq9aqlm1HetiPNoA27VqaX6jLzE_uHX1OBUI1kaP_gkuQaAXxClsV3G-wwUGKxtW-1eIVrKLNM44o&wd=&eqid=d66663b90004912d000000065c2b0f60)<br>
    [17推免（中国考研网）](http://www.chinakaoyan.com/info/article/id/146151.shtml)<br>


终于要开始学习机器学习了，之前偶尔看过，不成体系，更没有实践过。于是跟着莫烦机器学习的视频来学习，后面会有实战练习。光看视频，走马观花一般，一边下来，问问自己，好像什么也没记住，需要将学习到的知识在这里记录、梳理，并加深印象。

# 机器学习
## 什么是机器学习？

 ##### 机器学习是一种<font color=red>计算机理论</font>，是计算机科学家想让机器像人一样思考而发展出来的，包含<font color=red>概率论、统计学等数学知识。

* <font size=5, color=red>机器学习的一些应用：</font>Google now， Google photo，百度的图片识别都应用了机器学习。另外汇率预测、房价涨跌等一些应用也在探索和实践中发展起来。

* <font size=5, color=red>机器学习的方法</font>：即程序语言中所说的算法，算法有多种，目前所有方法大概分4-5类

1. <font color=mediumpurple >**监督学习（supervised learning）**</font>：带标签的数据让他学习，比如图片标明是猫或狗，然后给他这些图片去学习。神经网络就是一种监督学习的方式。

2. <font color=mediumpurple >**非监督学习（unsupervised learning）**</font>：没有标签的数据让他自己去发现数据背后的规律，比如只给猫和狗的图片，不告诉他哪些是猫、哪些是狗，让他把这个判断和分类，让他自己总结两种图片的不同。

<font  size=5 color=gree>给数据打标签是一件枯燥而低级的事情，但是估计分类效果更好，不然就不需要半监督学习了</font>

3. <font  color=mediumpurple>**半监督学习（semi-supervised learning）**</font>：综合监督学习和非监督学习特征，主要是想用少量带标签的数据和大量不带标签的数据进行训练和分类。
4.  <font  color=mediumpurple>**强化学习（reinforcement learning）**</font>：由规划机器人行为准则而来，让计算机在完全陌生的环境，自己学习成长，适应环境或者找到完成一项任务的方法途径。比如让机器人投篮，只给一个球，并告知命中得一分，然后他自己去适应调整，以得到高分。最初的表现可能会非常差，但是他经过总结、学习之后，最后会达到很高的命中率。AlphaGo即是用了这种方法。

5. <font  color=mediumpurple>**遗传算法--和强化学习类似（genetic algorithm）**</font>：通过模拟进化理论、淘汰弱者，来选择最优的设计或模型。比如让计算机学习玩超级玛丽，第一代可能很快就挂掉了，最后保存所有马里奥中最厉害的一个，第二代就基于他继续打怪，如此一代代下去，最终搞到一个高手高手高高手出来。

人工神经网络与生物神经网络





