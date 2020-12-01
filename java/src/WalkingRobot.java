public class WalkingRobot {
    public static int robotSim(int[] commands, int[][] obstacles) {
        int x = 0;
        int y = 0;
        int forward = 0;//north = 0 south = 1; west = 2 east = 3
        //how to judge the absolute direction?
        for(int i = 0;i<commands.length;i++){
            //当前数字指令
            int temp = commands[i];
            int oby = 0;
            int obx = 0;
            boolean hasOb = false;

            //1.前进
            if(temp>=1 && temp<=9){
                //在当前绝对方向上前进。
                //四种结果 x+=temp x-=temp y+=temp y-=temp
                //加入障碍物的判断:(x,y) (x',y')
                switch(forward){
                    case 0:
                        if(obstacles.length == 0){
                            y+=temp;
                        }
                        for(int j = 0;j<obstacles.length;j++){

                            //满足障碍物的条件
                            if( obstacles[j][0] == x && obstacles[j][1]>=y && obstacles[j][1]<=(y+temp)){
                                hasOb = true;
                                obx = obstacles[j][0];
                                oby = obstacles[j][1];

                                //y=oby-1;
                            }
                        }
                        // if(y!=oby-1){
                        //     y+=temp;
                        // }
                        //y+=temp;
                        break;
                    case 1:
                        if(obstacles.length == 0){
                            y-=temp;
                        }
                        for(int j = 0;j<obstacles.length;j++){
                            obx = obstacles[j][0];
                            oby = obstacles[j][1];
                            //满足障碍物的条件
                            if(obx == x && oby>=(y-temp) && oby<=y){
                                y=oby+1;
                            }
                        }
                        // if(y!=oby+1){
                        //    y-=temp;
                        // }
                        //y-=temp;
                        break;
                    case 2:
                        if(obstacles.length == 0){
                            x-=temp;
                        }
                        for(int j = 0;j<obstacles.length;j++){
                            obx = obstacles[j][0];
                            oby = obstacles[j][1];
                            //满足障碍物的条件
                            if(oby == y && obx>=(x-temp) && obx<=x){
                                x=obx+1;
                            }
                        }
                        // if(x!=obx+1){
                        //     x-=temp;
                        // }
                        //x-=temp;
                        break;
                    case 3:
                        if(obstacles.length == 0){
                            x+=temp;
                        }
                        for(int j = 0;j<obstacles.length;j++){
                            obx = obstacles[j][0];
                            oby = obstacles[j][1];
                            //满足障碍物的条件
                            if(oby == y && obx>=x && obx<=(x+temp)){
                                x=obx-1;
                            }
                        }
                        // if(x!=obx-1){
                        //     x+=temp;
                        // }
                        //x+=temp;
                        break;
                }

            }
            //2.方向改变：forward + left(-2)？  right(-1)？
            //left
            if(temp == -2){
                switch(forward){
                    case 0:forward = 2;break;
                    case 1:forward = 3;break;
                    case 2:forward = 1;break;
                    case 3:forward = 0;break;
                }

            }
            //right
            if(temp == -1){
                switch(forward){
                    case 0:forward = 3;break;
                    case 1:forward = 2;break;
                    case 2:forward = 0;break;
                    case 3:forward = 1;break;
                }
            }

        }
        return (x*x + y*y);

    }
    public static void main(String[] args) {
        double x = 7.0/3;
        System.out.println(x);
        //System.out.println(Math.ceil(2.333333));
        //Mat.ceil
    }
}
