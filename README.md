# lianjia_crawler
链家上海二手房信息爬取  
2019.2.25  
项目是做课程设计时完成的，有复用另一个B站爬虫的代码  
文件命名可能会引起混乱，这里一并解释一下  
f是first的意思，第一级  
sa和sb的s是second，a和b分别代表不同爬取过程的两个分支  
其中a分支爬取了在售房和小区信息，b分支爬取了已售房信息  
four就是第四级的意思  
area代表小区，sell代表在售，deal代表已售  

然后说一下为什么爬取房子的信息要通过小区来进行  
  在链家网直接查看二手房的信息是不能看到所有房子的，但是通过浏览小区，并修改url后面的页面信息可以完全访问所有的房产信息。所以在程序中有很多篇幅涉及到小区信息。  
  --------------
  讨论请发邮件至:stayallnight@163.com
