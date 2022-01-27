#!/usr/bin/env python3
import rospy
from ros_chatbot.srv import ActionService, ActionServiceResponse
import requests

class ActionTrigger:
    """Trigger an action in Rasa"""

    def __init__(self) -> None:
        """Just init the node"""
        pass

    def _action(self, req):
        """Triggers specific action passed in request.
        """

        url = 'http://localhost:5002/conversations/bot/execute?include_events=AFTER_RESTART'
        msg = {"name":req.action_name}
        r = requests.post(url,json=msg)

        return "ack"


    def start(self):
        """Initialize the node and start the services provided by this node.
        """
        rospy.init_node('trigger_action_service')
        rospy.Service('trigger_action', ActionService, self._action)
        rospy.spin()


if "__main__"==__name__:
    try:
        action_trigger = ActionTrigger()
        action_trigger.start()
    except rospy.ROSInterruptException as e:
        pass
