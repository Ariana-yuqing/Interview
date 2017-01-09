这次申请Twitter深受一亩三分地上小伙伴的福利，就来写个超详细的帖子！！
当时大致看了看大家的面经，感觉twitter热衷于考graph，于是吧CCIT上所有graph的题做了一遍，非常有用！！！

现在来说说题目吧。。
- OA：
    1. 很简单的data aggregation，给你很多data point，包括时间，时间类型，次数，然后给你个time range，print结果
    在我做完很久以后，有人发了面经，大家找找应该找得到。
    我当时觉得我code肯定是对的，但是test case就过了一个。然后我sort了一下，过了2个。
    所以我很肯定是print的格式不对，但是题目中什么都没有写。。在我做完OA以后，很愤怒的给了个差评。。。
    2. 我做完以后，leetcode上就有了。给你一个Gene bank，所有的Gene都是G T A C组成的，8位。
    给你一个start gene，一个end gene（表述比较奇怪，大家理解就好）。然后每次只能变一位，变异后的gene必须在bank里。
    求最少变异次数。
    就是一个比较normal的graph的题。但是当时一直不是超时就是超memory。
    BFS（这个就不多说了），因为每个node一共只有8*4个可能的变异，我是直接算所有的变异，然后check它在不在bank里。。blah blah
    但是注意的是，因为需要算距离，我当时是每个node同时存一个count，但是好像是超memory。
    我提交后，在leetcode上又做了一遍，然后突然醒悟，不需要存count，因为你访问每一层的时候，你是可以算出来这一层应该有多少个node
    然后直接先算node的个数，一个for loop就可以了，在这个for loop里的node都是一层的。

- 1st round interview：

⋅⋅⋅这一轮是一个小时的phone interview，一个coding question，再问一点experience
话说就让我介绍我最近做的一个project，问了两个随机的问题，就开始coding了
题目是，假设我们有一个新的字母表，a-z，但是顺序和现在的a-z不一样，可能是d，f，s，a 。。
你不知道这个字母表的顺序，然后给你a list of words。这些单词是按照新的字母表排序的。
找出新的字母表。
⋅⋅⋅ 第一眼看到这个题我是懵B的。。
然后想了想，这基本上就是个build order的题。
每个字母是一个node，根据相邻的两个word，你可以得到一个edge，代表谁在谁后面。
然后这样就可以建一个graph，之后BFS或者DFS找一个build order
我很纠结的跟她解释了一遍topological sort，然后发现她其实expect的是BFS。
不过她还是肯定了我的答案。
最后只写了个build_graph的function，然后测试了一下，她就给我过了。

- 2nd round：
一个实习给了我3个半小时的interview我也是谢谢他了。。
前15分钟跟一个帮我安排interview的妹子聊。然后3个back2back，最后跟HR来个并不开心的ending
    - 2-1: cultural questions，小哥基本上是在念问题，一个一个check。
       每次我回答完，就是next question， blah。。。。
       就是很基本的一些问题，第一个，why twitter。。T.T
    - 2-2: 我当时觉得我会fail就是这个问题答的很烂。。
       一开始，他给我出的题目，就是OA第二题，我纠结了半天，还是跟他说了。
       然后他换题。
       给你4张牌，可以用+ - * ／ exponentiation五个操作。找出最后结果是24的组合
       我当时是懵的，这个真的是懵的。。
       他给了一点hint
       假设这4张牌是  a b c d, 所有操作用 || 表示
       所有可能的combination有：
       a || b || c || d
       a || b || (c || d)
       a || (b || c || d)
       (a || b) || (c || d)
       a || (b || c ) || d
       然后就是a b c d的顺序问题，命中红心，我一直搞不清怎么写permutation
       然后我就默默纠结了10分钟，决定假设我已经有一个fixed order。写其他的code
       写完以后呢，他问我是想继续做permutation还是聊一聊improvement。
       果断聊优化啊，反正就头脑非常不清醒的B了一会，时间就已经到了，还超了10分钟。

- 2-3: 好像最后一个面的是一个manager之类的。先是问了一下我的experience。
       然后给了我一个class，还很nice的帮我把java改成了python。
       这个class有几个function：addNumber，getMean，getMedian
       一开始就用了很basic的做法，加数字的时候sort
       然后就有好几个followup

       - addNumber会call很多遍，但是其他两个会比较少。而且数字是从0-10000
       =》用一个array记录count，以及总共有多少个数字，getMedian的时候就search一遍
             （这里写了完整的code，并且test）

       - 可不可以O(1) getMedian
       =》记录下median的位置，每次加数字的时候，计算一遍会不会改变这个median，然后update

最后，祝大家都有好offer～～～笔芯