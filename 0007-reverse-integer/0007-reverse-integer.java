class Solution {
    public int reverse(int x) {
        
        if(x<=Integer.MIN_VALUE || x>=Integer.MAX_VALUE) return 0;
        
        double rev=0;
        int orginal = x;

        while(x!=0) {
            if(orginal>0) {
                int a = x%10;
                rev = rev*10 + a;
                x = x/10; 
                if(rev>=Integer.MAX_VALUE) {
                    rev = 0;
                    break;
                }
            } 
            else {
                x = Math.abs(x);
                int a = x%10;
                rev = rev*10 - a;
                x = x/10;
                if(rev<=Integer.MIN_VALUE) {
                    rev = 0;
                    break;
                }
            }
        }

        int result = (int)rev;
        return result;
    }
}