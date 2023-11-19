import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Main {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("FoodDash");
            frame.setSize(800, 500);
            frame.setLocation(300, 200);
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

            ImageIcon logoIcon = new ImageIcon("FoodDash_LogoWithName.png");
            JLabel logoLabel = new JLabel(logoIcon);
            logoLabel.setBounds(20, 5, 100, 100);

            ImageIcon icon = new ImageIcon("FoodDash_Icon.png");
            frame.setIconImage(icon.getImage());

            JLabel titleLabel = new JLabel("FoodDash");
            titleLabel.setFont(new Font("Elephant", Font.BOLD, 30));
            titleLabel.setForeground(new Color(255, 84, 4));
            titleLabel.setBounds(250, 30, 300, 40);

            JButton existingUserButton = new JButton("Existing User");
            existingUserButton.setFont(new Font("Arial", Font.BOLD, 15));
            existingUserButton.setForeground(Color.WHITE);
            existingUserButton.setBackground(new Color(255, 84, 4));
            existingUserButton.setBounds(250, 200, 300, 40);
            existingUserButton.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    showExistingUserPage();
                }
            });

            JButton newUserButton = new JButton("New User");
            newUserButton.setFont(new Font("Arial", Font.BOLD, 15));
            newUserButton.setForeground(Color.WHITE);
            newUserButton.setBackground(new Color(255, 84, 4));
            newUserButton.setBounds(250, 260, 300, 40);
            newUserButton.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    showNewUserPage();
                }
            });

            frame.setLayout(null);
            frame.add(logoLabel);
            frame.add(titleLabel);
            frame.add(existingUserButton);
            frame.add(newUserButton);

            frame.setVisible(true);
        });
    }

    private static void showExistingUserPage() {
        // Add logic to display the Existing User page
        System.out.println("Existing User Page");
    }

    private static void showNewUserPage() {
        // Add logic to display the New User page
        System.out.println("New User Page");
    }
}


