import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import SignIn2199502Navigator from '../features/SignIn2199502/navigator';
import SignUp2299501Navigator from '../features/SignUp2299501/navigator';
import BlankScreen099500Navigator from '../features/BlankScreen099500/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {

    //@BlueprintNavigationInsertion
SignIn2199502: { screen: SignIn2199502Navigator },
SignUp2299501: { screen: SignUp2299501Navigator },
BlankScreen099500: { screen: BlankScreen099500Navigator },

    /** new navigators can be added here */
    SplashScreen: {
      screen: SplashScreen
    }
};

const DrawerAppNavigator = createDrawerNavigator(
  {
    ...AppNavigator,
  },
  {
    contentComponent: SideMenu
  },
);

const AppContainer = createAppContainer(DrawerAppNavigator);

export default AppContainer;
