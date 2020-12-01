import java.util.*;

public class TowerHopper {
    class Tower{
        int index;
        Tower(int height){
            this.index = index;
        }
        boolean reached = false;


    }

//    Tower[] towers;
    List<Tower>[] towers;

    public void initGraph(int[] nums){
        towers = new List[nums.length];
        for (int i = 0; i <nums.length ; i++) {
            towers[i] = new ArrayList<>();
            towers[i].add(new Tower(i));
            for (int j = i+1; j <=nums[i] ; j++) {
                towers[i].add(new Tower(j));
            }
        }
    }
    public boolean bfsgetPath(){
        Queue<Tower> towerQueue = new LinkedList<>();
        towers[0].get(0).reached = true;
        towerQueue.offer(towers[0].get(0));
        while(!towerQueue.isEmpty()){
            Tower tmp = towerQueue.poll();
            for (Tower tower1: towers[tmp.index]) {
                if(tower1.reached == false){
                    tower1.reached = true;
                    towerQueue.offer(tower1);
                }

            }
        }
        return towers[towers.length-1].get(0).reached;
        //towers[0].get(0) =
        }

     public boolean dfsgetPath(){



        return false;
     }




    public static void main(String[] args) {
        int[] nums = {4,2,0,0,2,0};
        TowerHopper towerHopper = new TowerHopper();
        towerHopper.initGraph(nums);
        System.out.println(towerHopper.bfsgetPath());

    }
}
