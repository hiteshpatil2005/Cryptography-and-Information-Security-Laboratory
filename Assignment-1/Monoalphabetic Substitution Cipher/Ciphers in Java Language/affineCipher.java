import java.util.Scanner;

public class affineCipher {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the Plaintext : ");
        String plaintext = sc.nextLine();

        System.out.print("Enter the key : ");
        int a = sc.nextInt();

        System.out.print("Enter the key : ");
        int b = sc.nextInt();

        String cipher = encryptFunction(plaintext,a,b);
        System.out.print("The Encrypted message is : "+ cipher);

        sc.close();
    }

    public static String encryptFunction(String plaintext, int a, int b){
        String ciphertext = "";

        for(int i=0;i<plaintext.length();i++){
            char ch = plaintext.charAt(i);

            if(Character.isUpperCase(ch)){
                ch = (char)(((a * (ch - 'A') + b) % 26) + 'A');
            }

            else if(Character.isLowerCase(ch)){
                ch = (char)(((a * (ch - 'a') + b) % 26) + 'a');
            }

            ciphertext += ch;
        }
        return ciphertext;
    }
}
