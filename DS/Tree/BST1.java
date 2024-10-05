// Class to Create and Print the Expression Tree
import java.util.Scanner;


BST1d CreateTree(String s) {
    Stack<Node> st = new Stack<>();
    int len = s.length();

    for (int i = 0; i < len; i++) {
        char c = s.charAt(i);

        // If operand, create node and push to stack
        if (Character.isLetterOrDigit(c)) {
            Node newNode = new Node(c);
            st.push(newNode);
        } else {
            // Operator, pop two nodes and create subtree
            Node newNode = new Node(c);
            Node r = st.pop();
            Node l = st.pop();
            newNode.rchild = r;
            newNode.lchild = l;
            st.push(newNode); // Push subtree root to stack
        }
    }
    root = st.pop(); // Final node is the root of the tree
}

// Print the Expression Tree in a structured format
void PrintTree(Node x, int level) {
    if (x == null)
        return;
    PrintTree(x.rchild, level + 1); // Print right subtree
    for (int j = 0; j < level; j++)
        System.out.print("\t"); // Indentation based on level
    System.out.println(x.data); // Print the current node
    PrintTree(x.lchild, level + 1); // Print left subtree
}


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Postfix pf = new Postfix();
        ExpressionTree ext = new ExpressionTree();

        System.out.print("Enter an expression: ");
        String exp = sc.next(); // Get infix expression
        System.out.println("Given Expression is: " + exp);

        pf.ToPostfix(exp); // Convert infix to postfix
        exp = pf.result;
        System.out.println("Postfix Expression is: " + exp);

        ext.CreateTree(exp); // Create expression tree from postfix
        ext.PrintTree(ext.root, 1); // Print the expression tree
    }

    // Create the Expression Tree from Postfix Expression
    
