from netsimbridge.CSMANetwork import CSMANetwork
from lxdcontainer.LXDContainer import LXDContainer
import ns.core
import sys

ns.core.GlobalValue.Bind("SimulatorImplementationType", ns.core.StringValue("ns3::RealtimeSimulatorImpl"))
ns.core.GlobalValue.Bind("ChecksumEnabled", ns.core.BooleanValue("true"))

conleft = LXDContainer("con-left", "ubuntu:16.04")
conleft.create()

conright = LXDContainer("con-right", "ubuntu:16.04")
conright.create()

# conleft2 = LXDContainer("con-left2", "ubuntu:16.04")
# conleft2.create()

conleft.start()
# conleft2.start()
conright.start()

try:
    network = CSMANetwork(3, 100, 300)
    network.add_node(conleft, "10.199.199.2", "24")
    # network.add_node(conleft2, "10.199.199.3", "24")
    network.add_node(conright, "10.199.199.4", "24")

    # network = CSMANetwork(2, 100, 50)
    # network.add_node(conleft, "10.199.200.2", "24")
    # network.add_node(conleft2, "10.199.200.3", "24")

    ns.core.Simulator.Stop(ns.core.Seconds(6000))
    print("Start Simulation")
    ns.core.Simulator.Run(signal_check_frequency=-1)
    print("Simulation stopped")
except:
    print("Unexpected error:", sys.exc_info()[0])
    pass

print("Start cleanup")
ns.core.Simulator.Destroy()

conleft.destroy()
conright.destroy()
print("Clean Up Completed")