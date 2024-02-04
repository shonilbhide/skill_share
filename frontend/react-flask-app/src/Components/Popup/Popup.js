// Popup.js
import React, { useEffect, useRef } from 'react';
import './Popup.css';
import InputForm from '../InputForm';

const Popup = ({ callback, onClose }) => {
    const popupRef = useRef(null);

    const handleClickOutside = (event) => {
        if (popupRef.current && !popupRef.current.contains(event.target)) {
            onClose();
        }
    };

    useEffect(() => {
        document.addEventListener('mousedown', handleClickOutside);
        return () => {
            document.removeEventListener('mousedown', handleClickOutside);
        };
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);

    return (
        <div className="popup">
            <div ref={popupRef} className="popup-content">
                <button className="close-btn" onClick={onClose}>Close</button>
                <InputForm callback={callback} />
                {/* You can customize the content of the popup as needed */}
            </div>
        </div>
    );
};

export default Popup;
