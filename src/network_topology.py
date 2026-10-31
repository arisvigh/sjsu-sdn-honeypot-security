"""
*******************Honeypot in SDN******************************
SDN mininet network topology 

The topology consists five switches and each switch has 10 hosts

****************************************************************
"""

from mininet.topo import Topo

class MyTopo( Topo ):

    def __init__( self ):

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        switch1 = self.addSwitch( 's1' )
        switch2 = self.addSwitch( 's2' )
        switch3 = self.addSwitch( 's3' )
        switch4 = self.addSwitch( 's4' )
        switch5 = self.addSwitch( 's5' )
        
        for h in range(9):
                host = self.addHost('h2%s' % (h + 1))
                self.addLink(host, switch2)
        for h in range(9):
                host = self.addHost('h3%s' % (h + 1))
                self.addLink(host, switch3)
        for h in range(9):
                host = self.addHost('h4%s' % (h + 1))
                self.addLink(host, switch4)
        for h in range(9):
                host = self.addHost('h5%s' % (h + 1))
                self.addLink(host, switch5)


        # Add links
        self.addLink( switch1, switch2 )
        self.addLink( switch1, switch3 )
        self.addLink( switch1, switch4 )
        self.addLink( switch1, switch5 )
        self.addLink( switch2, switch3 )
        self.addLink( switch2, switch5 )
        self.addLink( switch3, switch4 )
        self.addLink( switch4, switch5 )


topos = { 'mytopo': ( lambda: MyTopo() ) }