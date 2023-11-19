import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class NewUser {
    private static JPanel cardPanel;
    private static CardLayout cardLayout;

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("FoodDash - New User");
            frame.setSize(800, 500);
            frame.setLocation(300, 200);
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

            cardLayout = new CardLayout();
            cardPanel = new JPanel(cardLayout);

            frame.add(cardPanel);

            // Add pages to the cardPanel
            cardPanel.add(createNewUserPanel(), "newUserPanel");
            // Add more pages as needed

            // Show the first page
            cardLayout.show(cardPanel, "newUserPanel");

            frame.setVisible(true);
        });
    }

    private static JPanel createNewUserPanel() {
        JPanel panel = new JPanel();
        panel.setLayout(null);

        // Existing code for the NewUser page

        JButton signUpButton = new JButton("Sign Up");
        signUpButton.setFont(new Font("Arial", Font.BOLD, 15));
        signUpButton.setForeground(Color.WHITE);
        signUpButton.setBackground(new Color(255, 84, 4));
        signUpButton.setBounds(280, 320, 200, 30);
        signUpButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Add logic for sign up action
                System.out.println("Sign Up Action");

                // Transition to the next page
                cardLayout.show(cardPanel, "nextPage"); // Replace "nextPage" with the identifier of the next page
            }
        });

        panel.add(signUpButton);

        return panel;
    }
}


