from fee_simulator.auction import AuctionState, Bid, FirstPriceAuction


class TestAuction:
    def test_add_bid_to_state(self):
        state = AuctionState()
        assert len(state.bids) == 0
        state.add_bid("agent1", 1000, 1000, 1)
        assert len(state.bids) == 1
    
    def test_remove_winning_bid_from_state(self):
        bid1 = Bid("agent3", 1300, 2000, 3)
        bid2 = Bid("agent5", 1200, 7000, 4)
        prev = {
            "bids": [ bid1, bid2 ],
            "bidHistory": [],
            "weightLimit": 11000000
        }
        state = AuctionState(prev=prev)
        assert len(state.bids) == 2

        state.remove_winning_bids([bid1])
        assert len(state.bids) == 1
        assert state.bids[0] == bid2

    def test_payment_dictionary(self):
        auction = FirstPriceAuction()
        assert 1
