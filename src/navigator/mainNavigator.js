import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import UserProfile207934Navigator from '../features/UserProfile207934/navigator';
import Tutorial207933Navigator from '../features/Tutorial207933/navigator';
import NotificationList207905Navigator from '../features/NotificationList207905/navigator';
import Settings207904Navigator from '../features/Settings207904/navigator';
import Settings207896Navigator from '../features/Settings207896/navigator';
import UserProfile207894Navigator from '../features/UserProfile207894/navigator';
import BlankScreen10171495Navigator from '../features/BlankScreen10171495/navigator';
import BlankScreen999509Navigator from '../features/BlankScreen999509/navigator';
import BlankScreen899508Navigator from '../features/BlankScreen899508/navigator';
import BlankScreen799507Navigator from '../features/BlankScreen799507/navigator';
import Settings499505Navigator from '../features/Settings499505/navigator';
import Maps699503Navigator from '../features/Maps699503/navigator';
import SignIn2199502Navigator from '../features/SignIn2199502/navigator';
import SignUp2299501Navigator from '../features/SignUp2299501/navigator';
import BlankScreen099500Navigator from '../features/BlankScreen099500/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {

    //@BlueprintNavigationInsertion
UserProfile207934: { screen: UserProfile207934Navigator },
Tutorial207933: { screen: Tutorial207933Navigator },
NotificationList207905: { screen: NotificationList207905Navigator },
Settings207904: { screen: Settings207904Navigator },
Settings207896: { screen: Settings207896Navigator },
UserProfile207894: { screen: UserProfile207894Navigator },
BlankScreen10171495: { screen: BlankScreen10171495Navigator },
BlankScreen999509: { screen: BlankScreen999509Navigator },
BlankScreen899508: { screen: BlankScreen899508Navigator },
BlankScreen799507: { screen: BlankScreen799507Navigator },
Settings499505: { screen: Settings499505Navigator },
Maps699503: { screen: Maps699503Navigator },
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
