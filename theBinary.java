import java.util.*;

public class theBinary {
    
    static class Node {
        Node lchild;
        int data;
        Node rchild;

        public Node(int data) {
            this.data = data;
            lchild = rchild = null;
        }
    }

    Node root = null; // Set root as null initially
    int height;

    void insertTree(int ele) {
        Node p, q;
        p = new Node(ele);
        if (root == null) {
            root = p; // Assign root directly if the tree is empty
        } else {
            q = root; // Start from the root
            while (true) {
                if (p.data <= q.data) {
                    if (q.lchild == null) {
                        q.lchild = p;
                        break;
                    } else {
                        q = q.lchild;
                    }
                } else {
                    if (q.rchild == null) {
                        q.rchild = p;
                        break;
                    } else {
                        q = q.rchild;
                    }
                }
            }
        }
    }

    boolean search(Node p, int val) { // Call search(root, val)
        if (p == null)
            return false;
        if (p.data == val)
            return true;

        if (val < p.data) {
            return search(p.lchild, val);
        } else {
            return search(p.rchild, val);
        }
    }

    void PrintTree(Node root, int i) {
        if (root == null)
            return;
        PrintTree(root.rchild, i + 1);
        for (int j = 0; j < i; j++) {
            System.out.print("\t"); // Corrected to print tab without newline
        }
        System.out.println(root.data);
        PrintTree(root.lchild, i + 1);
    }

    Node parent(Node p) {
        if (p == root)
            return null;
        Node q = root;
        while (q != null) {
            if (q.lchild == p || q.rchild == p)
                return q;
            if (p.data <= q.data)
                q = q.lchild;
            else
                q = q.rchild;
        }
        return null; 
    }

    boolean isleft(Node p) {
        Node q = parent(p);
        if (q == null)
            return false;
        return q.lchild == p;
    }

    boolean delete(Node p, int x) { // Call delete(root, val)
        Node q = p;
        Node parent = null;
        while (q != null && q.data != x) {
            parent = q;
            if (x < q.data)
                q = q.lchild;
            else
                q = q.rchild;
        }
        if (q == null) { // Element not found
            return false;
        }

        // Node with two children
        if (q.lchild != null && q.rchild != null) {
            Node max = findmax(q.lchild); // Find in-order predecessor
            q.data = max.data; // Replace with max of left subtree
            delete(q.lchild, max.data); // Remove the max node from left subtree
        } else {
            Node child = (q.lchild != null) ? q.lchild : q.rchild; // One child
            if (parent == null) { // Deleting root
                root = child;
            } else if (parent.lchild == q) {
                parent.lchild = child;
            } else {
                parent.rchild = child;
            }
        }
        return true;
    }

    void inOrder(Node p) {
        if (p == null)
            return;
        inOrder(p.lchild);
        System.out.print(p.data + " ");
        inOrder(p.rchild);
    }

    Node findmax(Node p) {
        while (p.rchild != null)
            p = p.rchild;
        return p;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        binary tree = new binary();
        
        int c, ele;
        binary.Node node = null;

        do {
            System.out.println("\n\n***BST***");
            System.out.println("1: Insert a Node");
            System.out.println("2: Delete a Node");
            System.out.println("3: Search a Node");
            System.out.println("4: Display The Tree");
            System.out.println("5: In-order Traversal");
            System.out.println("6: Exit");
            System.out.print("Enter the choice: ");
            
            c = sc.nextInt();

            switch (c) {
                case 1:
                    System.out.print("Enter element to insert: ");
                    ele = sc.nextInt();
                    tree.insertTree(ele);
                    System.out.println("Node inserted");
                    break;

                case 2: // Delete a Node
                    System.out.print("Enter element to delete: ");
                    ele = sc.nextInt();
                    if (tree.delete(tree.root, ele))
                        System.out.println("Node deleted");
                    else
                        System.out.println("Node not found");
                    break;

                case 3: 
                    System.out.print("Enter element to search: ");
                    ele = sc.nextInt();
                    if (tree.search(tree.root, ele))
                        System.out.println("Node found.");
                    else
                        System.out.println("Node not found.");
                    break;

                case 4:
                    tree.PrintTree(tree.root, 0);
                    break;

                case 5: 
                    tree.inOrder(tree.root);
                    System.out.println();
                    break;

                case 6:
                    System.out.println("Saionara");
                    break;

                default:
                    System.out.println("Invalid choice");
                    break;
            }
        } while (c != 6);

    }
}
