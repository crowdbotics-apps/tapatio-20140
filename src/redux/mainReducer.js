import { combineReducers } from "redux";

/**
 * You can import more reducers here
 */


//@BlueprintReduxImportInsertion
import SignIn2199502Reducer from '../features/SignIn2199502/redux/reducers'
import SignUp2299501Reducer from '../features/SignUp2299501/redux/reducers'

export const combinedReducers = combineReducers({
  blank: (state, action) => {
    if (state == null) state = [];
    return state;
  },


  //@BlueprintReduxCombineInsertion
SignIn2199502: SignIn2199502Reducer,
SignUp2299501: SignUp2299501Reducer,

});