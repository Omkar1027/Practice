public class t {
    public static void main (String[]args){
        int n=4;

        for(int r=1;r<=n;r++){
            for(int a=r;a>=(n-a);a--){
                System.out.print("*");
            }
            for(int b=r;b<=(1+n-b);b++){
                System.out.print(r);
            }
            System.out.println();
        }





    }
}
