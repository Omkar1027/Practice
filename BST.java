import java.util.Scanner;

public class BST {

    // NODE DECLARATION

    static class Node {
        Node left;
        int data;
        Node right;

        Node(int data) {
            this.data = data;
            this.left = null;
            this.right = null;
        }
    }

    static Node root;

    // INSERT FUNCTION

    void insertTree(int data) {
        Node p, q;
        p = new Node(data);
        if (root == null) {
            root = p;
        } else {
            q = root;
            while (true) {
                if (p.data <= q.data) {
                    if (q.left == null) {
                        q.left = p;
                        break;
                    } else {
                        q = q.left;
                    }
                } else {
                    if (q.right == null) {
                        q.right = p;
                        break;
                    } else {
                        q = q.right;
                    }
                }
            }
        }
    }

    // DELETE FUNCTION

    public static boolean delete(Node t, int x) {
        Node p;
        if (root == null) {
            System.out.println("The tree is empty");
            return false;
        }
        p = t;
        while (p != null && p.data != x) {
            if (x <= p.data) {
                p = p.left;
            } else {
                p = p.right;
            }
        }
        if (p == null) {
            System.out.println("Element not found");
            return false;
        }
        if (p.left == null && p.right == null) {
            if (parent(p) == null) {
                root = null;
                return true;
            }
            if (isleft(p)) {
                parent(p).left = null;
            } else {
                parent(p).right = null;
            }
            return true;
        } else if (p.left != null) {
            int val;
            Node ptr = findmax(p.left);
            val = ptr.data;
            delete(root, ptr.data);
            p.data = val;
        } else if (p == root) {
            root = p.right;
        } else {
            if (isleft(p)) {
                parent(p).left = p.right;
            } else {
                parent(p).right = p.right;
            }
        }
        return true;
    }

    // SEARCH FUNCN

    public static boolean search(Node p, int key) {
        if (p == null) {
            return false;
        }
        if (p.data == key) {
            return true;
        }
        if (key < p.data) {
            return search(p.left, key);
        } else {
            return search(p.right, key);
        }
    }

    //PRINT FUNCN

    public static void printTree(Node x, int i) {
        if (x == null) return;
        printTree(x.right, i + 1);
        for (int j = 0; j < i; j++) {
            System.out.print("\t");
        }
        System.out.print(x.data);
        System.out.println();
        printTree(x.left, i + 1);
    }

    // 3 TRAVERSALS

    public static void inorder(Node root) {
        if (root == null) return;
        inorder(root.left);
        System.out.print(root.data + " ");
        inorder(root.right);
    }

    public static void preorder(Node root) {
        if (root == null) return;
        System.out.print(root.data + " ");
        preorder(root.left);
        preorder(root.right);
    }

    public static void postorder(Node root) {
        if (root == null) return;
        postorder(root.left);
        postorder(root.right);
        System.out.print(root.data + " ");
    }

    // SUCESSOR

    public static Node successor(Node root, int key) {
        Node successor = null;
        Node current = root;
        while (current != null) {
            if (key < current.data) {
                successor = current;
                current = current.left;
            } else {
                current = current.right;
            }
        }
        return successor;
    }

    // PRECEDDOR

    public static Node predecessor(Node root, int key) {
        Node predecessor = null;
        Node current = root;
        while (current != null) {
            if (key > current.data) {
                predecessor = current;
                current = current.right;
            } else {
                current = current.left;
            }
        }
        return predecessor;
    }

    // MIN,MAX

    public static Node findmin(Node p) {
        if (p == null) return p;
        if (p.left == null) return p;
        return findmin(p.left);
    }

    public static Node findmax(Node p) {
        if (p == null) return p;
        if (p.right == null) return p;
        return findmax(p.right);
    }
    public static Node parent(Node p) {
        Node q = root;
        while (q != null) {
            if (q.left == p || q.right == p) return q;
            if (p.data < q.data) q = q.left;
            else q = q.right;
        }
        return null;
    }
    public static boolean isleft(Node p) {
        Node q = parent(p);
        return q != null && q.left == p;
    }

    public static void main(String args[]) {
        BST tree = new BST();
        Scanner sc = new Scanner(System.in);
        int choice, value;
        do {
            System.out.println("\n***BST***");
            System.out.println("1. Insert a Node");
            System.out.println("2. Delete a Node");
            System.out.println("3. Search a Node");
            System.out.println("4. Display The Tree");
            System.out.println("5. In-order Traversal");
            System.out.println("6. Pre-order Traversal");
            System.out.println("7. Post-order Traversal");
            System.out.println("8. Find Successor");
            System.out.println("9. Find Predecessor");
            System.out.println("10. Exit");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter value to insert: ");
                    value = sc.nextInt();
                    tree.insertTree(value);
                    break;
                case 2:
                    System.out.print("Enter value to delete: ");
                    value = sc.nextInt();
                    delete(root, value);
                    break;
                case 3:
                    System.out.print("Enter value to search: ");
                    value = sc.nextInt();
                    if (search(root, value)) {
                        System.out.println("Value found in the tree.");
                    } else {
                        System.out.println("Value not found.");
                    }
                    break;
                case 4:
                    System.out.println("Tree structure:");
                    printTree(root, 0);
                    break;
                case 5:
                    System.out.println("In-order traversal: ");
                    inorder(root);
                    System.out.println();
                    break;
                case 6:
                    System.out.println("Pre-order traversal: ");
                    preorder(root);
                    System.out.println();
                    break;
                case 7:
                    System.out.println("Post-order traversal: ");
                    postorder(root);
                    System.out.println();
                    break;
                case 8:
                    System.out.print("Enter value to find successor of: ");
                    value = sc.nextInt();
                    Node successor = successor(root, value);
                    if (successor != null) {
                        System.out.println("Successor is" + successor.data);
                    } else {
                        System.out.println("No Successor found.");
                    }
                    break;
                case 10:
                    System.out.print("Enter value to find predecessor: ");
                    value = sc.nextInt();
                    Node predecessor = predecessor(root, value);
                    if (predecessor != null) {
                        System.out.println("Predecessor is " + predecessor.data);
                    } else {
                        System.out.println("No Predecessor found.");
                    }
                    break;
                    case 11:
                    Node temp=findmin(root);
                    Sys
                    break;
                case 12:
                    System.out.println("Saionara");
                    break;
                default:
                    System.out.println("Invalid choice");
                    break;
            }
        } while (choice != 12);
        sc.close();
    }
}
