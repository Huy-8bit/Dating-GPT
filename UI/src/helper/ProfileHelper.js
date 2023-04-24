class ProfileHelper {
    static getNextProfileIdByHistory(history) {
        if (history.length === 0) {
            return 'P1';
        }
        
        const previousSender = history[history.length - 1].sender;
        return previousSender === 'P1' ? 'P2' : 'P1';
    }
    
    static areFilledProfiles(profiles) {
        if (!profiles) return false;

        return profiles.profile1 &&
            profiles.profile2 &&
            Object.keys(profiles.profile1).length !== 0 &&
            Object.keys(profiles.profile2).length !== 0;
    }
}

export default ProfileHelper;