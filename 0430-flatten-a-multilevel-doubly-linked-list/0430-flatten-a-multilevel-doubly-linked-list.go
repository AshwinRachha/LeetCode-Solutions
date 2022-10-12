/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Prev *Node
 *     Next *Node
 *     Child *Node
 * }
 */

func flatten(root *Node) *Node {
    curr := root
    for curr != nil {
        if curr.Child != nil {
            merge(curr)
        }
        curr = curr.Next
    }
    return root
}

func merge(current *Node) {
    child := current.Child
    for child.Next != nil {
        child = child.Next
    }
    if current.Next != nil {
        child.Next = current.Next
        current.Next.Prev = child
        
    }
    
    current.Next = current.Child
    current.Child.Prev = current
    
    current.Child = nil
}