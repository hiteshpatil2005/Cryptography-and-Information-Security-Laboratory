import java.util.Scanner;

class ceaserCipher{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the plaintext : ");
        String plaintext = sc.nextLine();

        System.out.println("Enter the key : ");
        int key = sc.nextInt();

        String encrypt = encryptFunction(plaintext, key);
        System.out.print("The cipher text is : "+encrypt);

        String decrypt = decryptFunction(encrypt,key);
        System.out.println("\nThe Decrypted message is : "+decrypt);

       sc.close();   
    }

    public static String encryptFunction (String plaintext, int key){
        
        String ciphertext = "";

        for (int i = 0; i < plaintext.length(); i++) {
            char ch = plaintext.charAt(i);

            if (Character.isUpperCase(ch)) {
                ch = (char) (((ch - 'A' + key) % 26) + 'A');
            } else if (Character.isLowerCase(ch)) {
                ch = (char) (((ch - 'a' + key) % 26) + 'a');
            }
            ciphertext += ch;
        }
        return ciphertext;
    }

    public static String decryptFunction(String cipher, int key){

        String pt = "";

        for(int i = 0; i < cipher.length(); i++){
            char ch = cipher.charAt(i);

            if(Character.isUpperCase(ch)){
                ch = (char)(((ch - 'A' - key + 26) % 26) + 'A');
            }

            else if (Character.isLowerCase(ch)) {
                ch = (char)(((ch - 'a' - key + 26) % 26) + 'a');
            }
            pt += ch;
        }
        return pt;
    }
}