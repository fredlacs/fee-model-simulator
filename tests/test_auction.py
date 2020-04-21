from fee_simulator.auction import AuctionState, Bid, FirstPriceAuction


class TestAuction:
    def test_add_bid_to_state(self):
        state = AuctionState()
        assert len(state.bids) == 0
        state.addBid("agent1", 1000, 1000, 1)
        assert len(state.bids) == 1
    
    def test_remove_winning_bid_from_state(self):
        bid = Bid("agent3", 1300, 2000, 3)
        prev = {
            "bids": [ bid ],
            "bidHistory": [],
            "weightLimit": 11000000
        }
        state = AuctionState(prev=prev)
        assert len(state.bids) == 1

        state.removeWinningBids(prev["bids"])
        assert len(state.bids) == 0


    def test_payment_dictionary(self):
        auction = FirstPriceAuction()
        assert 1

