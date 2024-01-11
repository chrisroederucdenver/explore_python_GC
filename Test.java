
/* interrogates and reports memory initially, after allocation of large chunk, and then after collection */
public class Test {


// https://stackoverflow.com/questions/17374743/how-can-i-get-the-memory-that-my-java-program-uses-via-javas-runtime-api

    private static final float DISPLAY_FACTOR = 1024L * 1024L;
    private static final int ARRAY_SIZE = 100000;
    private static void report_memory(String tag) {
        System.out.println(tag + " max:  " + (Runtime.getRuntime().maxMemory() / DISPLAY_FACTOR) );
        System.out.println(tag + " total:" + (Runtime.getRuntime().totalMemory() / DISPLAY_FACTOR) );
        System.out.println(tag + " free: " + (Runtime.getRuntime().freeMemory() / DISPLAY_FACTOR) );
        System.out.println(tag + " ffree:" + (getFairFreeMemory()/ DISPLAY_FACTOR) );
        System.out.println(tag + " used1: " + (getUsedMemory1() / DISPLAY_FACTOR) );
        System.out.println(tag + " used2: " + (getUsedMemory2() / DISPLAY_FACTOR) );
        System.out.println("");
    }

    private static long getUsedMemory1() {
        return Runtime.getRuntime().maxMemory() - Runtime.getRuntime().freeMemory();
    }
    private static long getUsedMemory2() {
        // https://stackoverflow.com/questions/17374743/how-can-i-get-the-memory-that-my-java-program-uses-via-javas-runtime-api
        return Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();
    }
    private static long getFairFreeMemory() {
        return Runtime.getRuntime().maxMemory() - getUsedMemory2();
    }

    public static void main(String args[]) {
  
        //report_memory("initially       "); 
        long initial_used_memory = getUsedMemory2();
        System.out.println("Initial  used memory:" + (initial_used_memory / DISPLAY_FACTOR));

        //Integer[] integer_array = new Integer[ARRAY_SIZE];
        int[] integer_array = new int[ARRAY_SIZE];
        try { Thread.sleep(100); /* ms */ } // desperate attempt to see impact of the allocation
        catch (Exception e) { System.out.println("caught an exception" + e); }
        long allocated_used_memory = getUsedMemory2();
        System.out.println("Change in used memory:" + (initial_used_memory - allocated_used_memory) / DISPLAY_FACTOR);
        //report_memory("after allocation"); 

        System.gc();
        long freed_used_memory = getUsedMemory2();
        System.out.println("Change in used memory:" + (allocated_used_memory - freed_used_memory) / DISPLAY_FACTOR);
        //report_memory("after collection"); 
    }   

}
