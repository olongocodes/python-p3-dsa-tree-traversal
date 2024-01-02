class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, target_id):
        return self.depth_first_traversal(self.root, target_id)

    def depth_first_traversal(self, current_node, target_id):
        if current_node is None:
            return None

        if current_node.get('id') == target_id:
            return current_node

        for child in current_node.get('children', []):
            result = self.depth_first_traversal(child, target_id)
            if result:
                return result

        return None

    def get_element_by_id_breadth_first(self, target_id):
        queue = [self.root]

        while queue:
            current_node = queue.pop(0)

            if isinstance(current_node, dict) and current_node.get('id') == target_id:
                return current_node

            if isinstance(current_node, dict):
                queue.extend(current_node.get('children', []))

        return None

# Example Usage:
# Assuming you have a Tree instance named 'my_tree'
# tree = Tree(your_root_node)

# Create an instance of the Tree class
my_tree = Tree('your_root_node')

# Depth-First Traversal
result_depth_first = my_tree.get_element_by_id('heading')
print(result_depth_first)

# Breadth-First Traversal
result_breadth_first = my_tree.get_element_by_id_breadth_first('your_target_id')
print(result_breadth_first)
