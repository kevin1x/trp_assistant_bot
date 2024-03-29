import * as actionType from '../actions/types';

const tokenInitialState = {
  token: localStorage.getItem('token') || null,
  username: '',
  isLogined: false
};

export default (state = tokenInitialState, action) => {
  switch(action.type) {
    case actionType.SET_TOKEN:
      localStorage.setItem('token', action.data.token);
      return {
        ...state, 
        token: action.data.token, 
        username: action.data.username, 
        isLogined: action.data.isLogined
      };
    default:
      return state;
  }
}
