import java.math.BigInteger;
import java.util.Scanner;

public class DiffieHellman {
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a prime number (q): ");
        BigInteger prime = sc.nextBigInteger();

        System.out.print("Enter a primitive root modulo q (alpha): ");
        BigInteger g = sc.nextBigInteger();

        System.out.print("Enter value of Xa: ");
        BigInteger privateKeyAlice = sc.nextBigInteger();

        System.out.print("Enter value of Xb: ");
        BigInteger privateKeyBob = sc.nextBigInteger();

        BigInteger publicKeyAlice = g.modPow(privateKeyAlice, prime); 
        BigInteger publicKeyBob   = g.modPow(privateKeyBob, prime);   

        System.out.println("\nPublic Key Calculation");
        System.out.println("Xa's Public Key: "+ publicKeyAlice);
        System.out.println("Xb's Public Key: "+ publicKeyBob);

        BigInteger sharedSecretAlice = publicKeyBob.modPow(privateKeyAlice, prime); 
        BigInteger sharedSecretBob   = publicKeyAlice.modPow(privateKeyBob, prime); 

        System.out.println("\n Shared Secret Calculation");
        System.out.println("Shared Secret (Ya): "+ sharedSecretAlice);
        System.out.println("Shared Secret (Yb): "+ sharedSecretBob);

        if (sharedSecretAlice.equals(sharedSecretBob)) 
        {
            System.out.println("\n Both parties share the same secret key: " + sharedSecretAlice);
        } 
        else 
        {
            System.out.println("\n Secrets do not match.");
        }
        sc.close();
    }
}
