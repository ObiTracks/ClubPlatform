import React from 'react';
import StripSmall from './StripSmall';
import StripLarge from './StripLarge';
export default function Card() {
    return (
        <div className="genericCard">
            <div>Generic Card</div>
            <div>
                <StripSmall />
                <StripSmall />
                <StripLarge />
                {/* {this.props.children} */}
            </div>
        </div>
    )
}
