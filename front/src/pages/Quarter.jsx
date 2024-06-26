import React from 'react';
import { useNavigate } from 'react-router-dom';
import RoundNavBar from "../components/QuarterPageComp/RoundNavBar";
import Tournament from "../components/QuarterPageComp/Tournament";
import { currentRoundState, totalRoundsState } from "../atom/atom";
import { useRecoilValue } from "recoil";

function Quarter() {
    const navigate = useNavigate();
    const currentRound = useRecoilValue(currentRoundState);
    const totalRounds = useRecoilValue(totalRoundsState);

    const handleRoundsComplete = (selectedImages) => {
        navigate('/select', { state: { selectedImages } });
    };

    return (
        <div>
            <RoundNavBar currentRound={currentRound} totalRounds={totalRounds} />
            <Tournament onRoundsReady={handleRoundsComplete} />
        </div>
    );
}

export default Quarter;