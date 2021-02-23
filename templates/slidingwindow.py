# public class Solution {

#     public String minWindow(String s, String t) {
#         // 同方向移动，起始的时候，都位于 0，表示我们定义搜索区间为 [left, right) ，此时区间为空区间
#         int left = 0;
#         int right = 0;

#         while (right < sLen) {

#             if ( 在右移的过程中检测是否满足条件 ) {
#                 // 对状态做修改，好让程序在后面检测到满足条件
#             }

#             // 右边界右移 1 格
#             right++;

#             while ( 满足条件 ) {

#                 // ① 走到这里是满足条件的，左边界逐渐逐渐左移，可以取最小值

#                 if ( 在左移的过程中检测是否不满足条件 ) {
#                     // 对状态做修改，好让程序在后面检测到不满足条件
#                 }

#                 // 左边界左移 1 格
#                 left++;
#             }
#             // ② 走到这里是不满足条件的，右边界逐渐右移，可以取最大值
#         }
#         return 需要的结果变量;
#     }
# }

# def min_window(s, t):
#     left = 0
#     right = 0
#     while (right < len(s)):
#         if 