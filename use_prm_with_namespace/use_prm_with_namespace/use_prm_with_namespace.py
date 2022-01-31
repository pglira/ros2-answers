import rclpy
from rclpy.node import Node


class TestNode(Node):
    def __init__(self):
        super().__init__("use_prm_with_namespace")

        self.get_logger().info("Start node")

        # prm "foo" without namespace
        self.declare_parameters(namespace="", parameters=[("foo", "default_value_foo")])

        # prm "bar" with namespace "ns1"
        self.declare_parameters(
            namespace="ns1",
            parameters=[("bar", "default_value_bar_ns1")],
        )

        # prm "bar" with namespace "ns2"
        self.declare_parameters(
            namespace="ns2",
            parameters=[("bar", "default_value_bar_ns2")],
        )

        print(f'foo = {self.get_parameter("foo").value}')
        print(f'bar_ns1 = {self.get_parameter("ns1.bar").value}')
        print(f'bar_ns2 = {self.get_parameter("ns2.bar").value}')


def main(args=None):
    rclpy.init(args=args)
    node = TestNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
